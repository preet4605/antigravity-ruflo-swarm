---
name: android-navigation-expert
description: "Use when scaffolding or debugging Jetpack Compose Navigation. Enforces Type-Safe navigation with Kotlin Serialization instead of legacy String routes."
category: architecture
risk: low
source: community
date_added: "2026-03-31"
metadata:
  triggers:
    - "@navigation"
    - "compose-navigation"
    - "nav_graph"
    - "type-safe-navigation"
    - "navcontroller"
---

# Type-Safe Compose Navigation 🧭🚀

A strict guideline prohibiting legacy string-based navigation in Jetpack Compose, enforcing the modern Kotlinx Serialization approach for robust, crash-free routing.

## ⚡ When to Use
- **Creating a NavHost**: Scaffolding the screen routing for a new app.
- **Passing Arguments**: Sending IDs, details, or objects between screens.
- **Refactoring Navigation**: Upgrading a codebase from string-based routes to Type-Safe routes.

## 🚫 The Anti-Pattern (String Routes)
**NEVER DO THIS.** AI Agents trained on older data routinely hallucinate this pattern. It is fragile, cannot pass complex objects easily, and crashes frequently if strings are mismatched:
```kotlin
// BAD - DO NOT USE
navController.navigate("profile/${user.id}")
```

## ✅ The Standard (Type-Safe Navigation)
**ALWAYS DO THIS.** Use Compose Navigation 2.8.0+ and `kotlinx.serialization`.

### 1. Define Routes as Data Objects/Classes
In your presentation layer, define the screens using `@Serializable`.
```kotlin
import kotlinx.serialization.Serializable

@Serializable
object HomeRoute

@Serializable
data class ProfileRoute(val userId: String, val isLoggedIn: Boolean)
```

### 2. Scaffold the NavHost
Use the objects/classes directly in the `NavHost` builder.
```kotlin
NavHost(navController = navController, startDestination = HomeRoute) {
    composable<HomeRoute> {
        HomeScreen(
            onNavigateToProfile = { id -> 
                navController.navigate(ProfileRoute(userId = id, isLoggedIn = true))
            }
        )
    }
    composable<ProfileRoute> { backStackEntry ->
        // Extract arguments safely!
        val profile: ProfileRoute = backStackEntry.toRoute()
        ProfileScreen(userId = profile.userId)
    }
}
```

### 3. Agent Guardrails for Navigation
1. **Dependencies**: Ensure `androidx.navigation:navigation-compose:2.8.+` and `org.jetbrains.kotlinx:kotlinx-serialization-json` are in the `build.gradle.kts`.
2. **Plugins**: Ensure `alias(libs.plugins.kotlin.serialization)` is applied in the module-level `build.gradle.kts`.
3. **No Strings Attached**: If you type `"/"` or `"?"` inside a `navigate()` call, you are breaking the rules of this workspace. Use `@Serializable` data classes.
