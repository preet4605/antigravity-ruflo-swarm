---
name: android-detekt-expert
description: "Use when performing logic-based static analysis, detecting code smells, or configuring Detekt for Android."
category: quality
risk: low
source: community
date_added: "2026-03-31"
metadata:
  triggers:
    - "@detekt"
    - "code-smell"
    - "static-analysis"
    - "complexity-check"
    - "debt-management"
---

# Android Detekt Logic Analysis 🧐🔍

Advanced strategies for detecting hidden logic errors, structural flaws, and code debt in Kotlin Android applications.

## ⚡ When to Use
- **Code Smell Hunting**: Identifying long functions, deeply nested loops, or excessive cognitive complexity.
- **Architectural Guardrails**: Enforcing rules like "No `viewModelScope.launch` outside of ViewModels".
- **Naming Enforcement**: Ensuring all interfaces end with `Interface` (if that's the team policy).
- **Refactoring Strategy**: Identifying the most "complex" files that need simplification first.
- **CI/CD Quality Gate**: Failing a build based on logic violations.

## 🏗️ Core Categories

### 1. Complexity
- **TooManyFunctions**: Aim for < 11 functions per class.
- **LongMethod**: Aim for < 20 lines per function.
- **NestedBlockDepth**: Aim for < 4 levels of nesting.

### 2. Formatting (Logic-Based)
- **OptionalUnit**: Don't return `Unit` explicitly.
- **UnusedPrivateMember**: Delete unused variables and functions.
- **RedundantVisibilityModifier**: Keep it clean if defaults are sufficient.

### 3. Potential Bugs
- **EqualsWithHashCode**: Always override both together.
- **UnreachableCode**: Remove code that can't be executed.
- **UnsafeCallOnNullableType**: Avoid using `!!` operator.

### 4. Style & Naming
- **ForbiddenMethodCall**: Block usage of certain libraries (e.g., `java.util.Date` in favor of `java.time` or `kotlinx-datetime`).
- **ForbiddenImport**: Prevent importing internal or deprecated classes.

## 🛠️ Essential Commands

### Check Logic Errors
```bash
./gradlew detekt
```

### Auto-Correct (Basic)
```bash
./gradlew detekt --auto-correct
```

## 📜 Configuration (`detekt.yml`)

Use a custom configuration file to override default thresholds:
```yaml
complexity:
  TooManyFunctions:
    active: true
    thresholdInFiles: 11
    thresholdInClasses: 11
    thresholdInInterfaces: 11
    thresholdInObjects: 11
  LongMethod:
    active: true
    threshold: 20
```

## 🚀 Performance & Tips

- [ ] **Custom Rules**: Implement `Rule` subclass to enforce project-specific requirements.
- [ ] **Baseline Files**: Use `detekt-baseline.xml` for large existing projects to prioritize fixing new issues.
- [ ] **IDE Integration**: Install the "Detekt" plugin in Android Studio/IntelliJ.

## 🧪 Verification Checklist

- [ ] **No Complex Functions**: Logic is broken down into small, testable units.
- [ ] **No Dead Code**: All private members are used or deleted.
- [ ] **Stable APIs**: All public APIs follow consistent naming and documentation rules.
- [ ] **No Deprecated Usage**: Modern APIs are used exclusively.

## 🔗 Related Resources
- [Official Detekt Documentation](https://detekt.dev)
- [Code Review Expert](../android-code-review-expert/SKILL.md)
- [Kotlin Lint & Quality](../android-lint-and-quality/SKILL.md)
