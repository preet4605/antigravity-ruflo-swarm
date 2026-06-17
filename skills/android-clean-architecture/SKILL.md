---
name: android-clean-architecture
description: "Use when designing the architecture, data layer, domain models, or business logic for Android apps."
category: architecture
risk: low
source: community
date_added: "2026-03-31"
metadata:
  triggers:
    - "@clean-architecture"
    - "data-layer"
    - "domain-layer"
    - "presentation-layer"
    - "use-case"
    - "repository-pattern"
---

# Android Clean Architecture Excellence 🏗️

Standardized architectural patterns for scalable, testable, and maintainable Android applications.

## ⚡ When to Use

- **App Structure**: Planning or refactoring the module/package layout.
- **Data Fetching**: Implementing Retrofit or Room repositories.
- **Business Logic**: Writing Use Cases or Interactors.
- **UI Architecture**: Choosing between MVI, MVVM, or custom patterns.
- **State Management**: Consuming data from Flow/StateFlow in ViewModels.

## 🏗️ The Three Pillars

### 1. Presentation Layer (UI & ViewModels)

- **Pattern**: Always use **Jetpack ViewModel**.
- **State**: Use `MutableStateFlow` in ViewModel. In Compose UI, ALWAYS collect using `collectAsStateWithLifecycle()` (requires `androidx.lifecycle:lifecycle-runtime-compose`). NEVER use `collectAsState()` as it wastes resources in the background.
- **MVI/MVVM**: Prefer **State + Events + Effects** for complex screens.
- **Anti-Pattern (No Stubs)**: NEVER generate stubbed empty callbacks (e.g., `onClicked = { /* Future implementation */ }`) when scaffolding. If tasked to build a feature, ALWAYS implement the full event flow from UI to ViewModel to Repository.
- **Navigation**: Use **Compose Navigation** with Safe Args (Type-safe routing via Kotlinx Serialization) instead of manual screen swapping.

### 2. Domain Layer (The Core)

- **Rule**: NO Android dependencies (except maybe `@Inject`). Pure Kotlin.
- **Use Cases**: Each Use Case should have a single responsibility.

  ```kotlin
  class GetUserUseCase @Inject constructor(private val repository: UserRepository) {
      operator fun invoke(id: String): Flow<User> = repository.getUser(id)
  }
  ```

- **Models**: Pure Kotlin data classes (Domain-specific). 
- **CRITICAL ANTI-HALLUCINATION GUARD**: NEVER assume or guess the properties of a data class (e.g., guessing a `TodoItem` has a `dueDate`). You MUST explicitly read the data classes in `domain/model/` before writing ViewModel or Repository mapping logic to prevent `Unresolved reference` or constructor errors.

### 3. Data Layer (Sources & Repositories)

- **Pattern**: Repository as a single source of truth.
- **DTOs**: Data Transfer Objects (e.g., Json objects from Retrofit). Always map DTOs to Domain Models before passing to the Domain Layer.
- **Sources**: Remote (Retrofit/Ktor) and Local (Room/DataStore).
- **Room TypeConverters (CRITICAL)**: If your domain model contains non-primitive types (e.g., `LocalDateTime`, Enums, Custom Objects), you MUST create a `@TypeConverter` class and explicitly register it on the `@Database` class before compiling. Room cannot natively store them!

## 💉 Dependency Injection (Hilt)

Hilt is the standard DI library. Ensure the following foundational setup is ALWAYS present:

### 1. Mandatory Application Class
- **Rule**: Create a class inheriting from `Application` and annotate it with `@HiltAndroidApp`.
  ```kotlin
  @HiltAndroidApp
  class BaseApplication : Application()
  ```

### 2. Manifest Registration
- **Rule**: Register your application class in `AndroidManifest.xml` using `android:name=".BaseApplication"`.

### 3. Usage Patterns
- Use `@HiltViewModel` for ViewModels.
- Use `@AndroidEntryPoint` for Activities/Fragments (if any).
- Use `@Inject constructor` for Use Cases and Repositories.
- Create `@Module` and `@InstallIn(SingletonComponent::class)` for platform dependencies.

## 🧪 Testing Strategy

- **Unit Tests**: Place in `test/`. Use **MockK** for mocking interfaces.
- **Test Coroutines**: Use `runTest` and `TestDispatcher`.
- **Fakes vs Mocks**: Prefer **Fakes** for complex Data sources and **Mocks** for simple verification.

## 🚀 Modern Reactive Flows

- [ ] **StateFlow**: For state that needs initial value and persistence.
- [ ] **SharedFlow**: For one-off events (e.g., Navigation, Snackbar).
- [ ] **Error Handling**: Use a `Result` wrapper or `Resource` object to encapsulate Success/Error states.

## 🔗 Related Resources

- [Google Official Architecture Guide](https://developer.android.com/topic/architecture)
- [Compose Skill](../android-jetpack-compose/SKILL.md)
