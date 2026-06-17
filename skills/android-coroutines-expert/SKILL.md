---
name: android-coroutines-expert
description: "Use to enforce safe concurrency, correct Dispatcher usage, and proper Channel vs StateFlow patterns in ViewModels."
category: performance
risk: medium
source: community
date_added: "2026-03-31"
metadata:
  triggers:
    - "@coroutines"
    - "concurrency"
    - "flow-vs-channel"
    - "viewmodelscope"
    - "dispatchers"
---

# Coroutines & Concurrency Mastery ⚡🧵

A strict rulebook to prevent thread-blocking, memory leaks, and lost UI events in modern Android applications.

## ⚡ When to Use
- **ViewModel Logic**: Launching coroutines for network/database requests.
- **One-Time UI Events**: Showing Snackbars, Toasts, or Navigation triggers.
- **Parallel Work**: Running multiple non-blocking tasks.

## 🚦 Rule 1: The UI Event Dilemma (StateFlow vs Channel)

You must explicitly distinguish between **UI State** (things that persist on rotation) and **UI Events** (things that happen once, like a Toast or Navigation).

- **UI STATE**: Use `MutableStateFlow`.
- **UI EVENTS**: Use an un-buffered `Channel` exported as a `Flow`. **NEVER** use `SharedFlow` with `replay = 0` or `MutableStateFlow` for one-time events, because if the app rotates, the event might be dropped or replayed twice.

**The Golden Implementation:**
```kotlin
class MyViewModel : ViewModel() {
    // 1. UI STATE
    private val _uiState = MutableStateFlow(MyState())
    val uiState = _uiState.asStateFlow()

    // 2. ONE-TIME EVENTS
    private val _uiEvent = Channel<MyAction>()
    val uiEvent = _uiEvent.receiveAsFlow()

    fun triggerSnackbar() {
        viewModelScope.launch {
             _uiEvent.send(MyAction.ShowSnackbar)
        }
    }
}
```

## 🚥 Rule 2: Dispatcher Discipline
Agents frequently launch heavy database or network calls on the default dispatcher (`Dispatchers.Main` inside a `viewModelScope.launch`).

- **Rule**: If you are using Retrofit or Room, they are naturally "main-safe", so `viewModelScope.launch { }` is fine.
- **Rule**: If you are doing manual file I/O, heavy JSON parsing, or bitmap manipulation, you **MUST** switch to `Dispatchers.IO` using `withContext(Dispatchers.IO) { ... }`.
- **Rule**: If you are doing CPU-heavy sorting or filtering on massive lists, use `Dispatchers.Default`.

## 🛑 Rule 3: Structured Concurrency
If an agent executes multiple independent API requests inside a `viewModelScope.launch`, and one fails, it cancels the entire scope/parent job!

**The Anti-Pattern:**
```kotlin
viewModelScope.launch {
    // If ApiA fails, ApiB is cancelled!
    val resultA = apiA.fetch() 
    val resultB = apiB.fetch()
}
```

**The Architect's Standard (supervisorScope or async):**
```kotlin
viewModelScope.launch {
    // Both attempt to run. If A fails, B continues successfully.
    supervisorScope {
        val deferredA = async { apiA.fetch() }
        val deferredB = async { apiB.fetch() }
        
        try { val a = deferredA.await() } catch (e: Exception) {}
        try { val b = deferredB.await() } catch (e: Exception) {}
    }
}
```

## 🔋 Rule 4: collectAsStateWithLifecycle
As enforced in our Code Review checklists, NEVER use `collectAsState()` in Compose UI. Always use `collectAsStateWithLifecycle()` to ensure Coroutines pause fetching when the screen goes to the background.
