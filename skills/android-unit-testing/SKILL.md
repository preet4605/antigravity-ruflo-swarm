---
name: android-unit-testing
description: "Use when writing or fixing unit tests, mocking objects, or testing reactive flows in Android."
category: testing
risk: low
source: community
date_added: "2026-03-31"
metadata:
  triggers:
    - "@android-testing"
    - "junit-5"
    - "mockk"
    - "turbine-testing"
    - "unit-test"
---

# Android Unit Testing Excellence 🧪🛡️

The ultimate guide to writing robust, reliable, and maintainable unit tests for Android applications using modern tools like MockK, Turbine, and Coroutine Test.

## ⚡ When to Use

- **Business Logic Verification**: Testing Use Cases or ViewModels.
- **Data Layer Testing**: Testing Repositories or Data Sources (with Fakes).
- **Reactive Stream Testing**: Verifying emitted values from `Flow` and `StateFlow`.
- **Logic Refactoring**: Ensuring no regressions during code changes.
- **TDD (Test-Driven Development)**: Writing tests before implementation.

## 🏗️ Core Tools

### 1. JUnit 5 (Modern Standard)

- Use `@Test`, `@BeforeEach`, and `@DisplayName` for clear tests.
- **Rule**: Prefer JUnit 5 for new projects, but JUnit 4 is common in legacy.

### 2. MockK (Power Mocking)

- **Rule**: Use MockK for Kotlin-first mocking.
- **Shorthand**: `every { ... } returns ...` and `coEvery { ... } returns ...` for suspend functions.
  ```kotlin
  val repository = mockk<UserRepository>()
  coEvery { repository.getUser("123") } returns User("John")
  ```

### 3. Turbine (Flow Testing)

- **Rule**: Never use `collect` or `first()` in tests manually. Use Turbine.
  ```kotlin
  flow.test {
      assertEquals(1, awaitItem())
      assertEquals(2, awaitItem())
      awaitComplete()
  }
  ```

## 🚀 Coroutine Testing (Essentials)

### Use `runTest`

- `runTest` skips `delay()` and ensures tests run fast and predictably.

### Inject Dispatchers

- **Rule**: NEVER hardcode `Dispatchers.IO` or `Main`. Inject them.
- **In Tests**: Use `StandardTestDispatcher` or `UnconfinedTestDispatcher`.

## 🧪 Testing Patterns

### 1. ViewModels

- **Standard**: Test the Initial State → Trigger Action → Verify Final State and/or Side Effects.
- **Note**: Ensure `Dispatchers.setMain(testDispatcher)` is called before and `Dispatchers.resetMain()` after tests.

### 2. Repositories

- **Standard**: Test that data is correctly mapped and error handling is resilient.
- **Fakes**: Use `FakeLocalSource` or `FakeRemoteSource` for complex integration tests.

### 3. Domain Use Cases

- **Standard**: Test that the use case calls the repository and applies business rules correctly.

## 📦 Assertion Libraries

- **Truth (from Google)**: Fluent, readable assertions.
- **AssertJ**: Extremely powerful and comprehensive.
- **Kotest Assertions**: Native Kotlin syntax (e.g., `user.name shouldBe "John"`).

## 🚀 Testing Checklist

- [ ] **Method Names**: Use descriptive names like `test_whenQueryChanged_updatesState`.
- [ ] **One Assertion per Test**: (Ideally) One logical assertion per test for better failure isolation.
- [ ] **Arrange-Act-Assert (AAA)**: Follow this structure for readability.
- [ ] **Verify Mocks**: Check if expected methods were called using `verify { ... }`.

## 🔗 Related Resources

- [Testing Best Practices (Google)](https://developer.android.com/training/testing)
- [MockK Reference](https://mockk.io)
- [Turbine Documentation](https://github.com/cashapp/turbine)
