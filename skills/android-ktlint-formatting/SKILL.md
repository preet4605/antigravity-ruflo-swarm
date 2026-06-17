---
name: android-ktlint-formatting
description: "Use when formatting Kotlin code, enforcing the Android style guide, or configuring KtLint for Android."
category: quality
risk: low
source: community
date_added: "2026-03-31"
metadata:
  triggers:
    - "@ktlint"
    - "kotlin-format"
    - "style-guide"
    - "reformatting"
    - "ktlint-check"
---

# Android KtLint Formatting Excellence 🧹💎

Standardized formatting rules for Android developers based on the official Kotlin and Android Style Guides.

## ⚡ When to Use
- **Code Cleanup**: Automatically reformatting messy files.
- **Pre-commit Audit**: Ensuring the code is perfectly formatted before pushing.
- **CI/CD Configuration**: Setting up a gatekeeper for code style.
- **New Project Setup**: Initializing a project with the correct `.editorconfig`.

## 🏗️ Core Rules (Android Style)

### 1. Indentation
- Use **4 spaces** for indentation.
- No TAB characters allowed.
- Follow "Continuation Indents" for long method calls (8 spaces).

### 2. Imports
- **Rule**: Avoid wildcard imports (`import com.example.*`).
- Order alphabetically.
- Group by `java.*`, `kotlin.*`, then external libraries.

### 3. Blank Lines
- Single blank line between classes, properties, and methods.
- NO trailing whitespace at the end of lines.
- NO multiple blank lines.

### 4. Naming
- **Classes/Interfaces**: `PascalCase`.
- **Properties/Variables**: `camelCase`.
- **Functions**: `camelCase`.
- **Constants**: `SCREAMING_SNAKE_CASE`.

## 🛠️ Essential Commands

### Check Formatting
```bash
./gradlew ktlintCheck
```

### Auto-Fix Formatting
- **Rule**: ALWAYS run this before committing if formatting changes are extensive.
```bash
./gradlew ktlintFormat
```

## 📜 Configuration (`.editorconfig`)

Ensure your project has a `.editorconfig` that KtLint reads:
```ini
[*.{kt,kts}]
indent_size=4
insert_final_newline=true
max_line_length=120
ij_kotlin_allow_trailing_comma=true
```

## 🚀 Performance & Tips

- [ ] **IDE Integration**: Install the "KtLint" or "Kotlin" plugin and enable "On Save" actions.
- [ ] **Trailing Comma**: Use trailing commas for all multi-line collections and arguments for better diffs.
- [ ] **Imports Cleanup**: Periodically run `Alt+Enter` → "Optimize Imports".

## 🧪 Verification Checklist

- [ ] **No Wildcards**: All imports are explicit.
- [ ] **No Tabs**: Only spaces.
- [ ] **EndOfLine**: File ends with exactly one newline.
- [ ] **No Redundant Semicolons**: Clean up all unnecessary `;`.

## 🔗 Related Resources
- [Official Pinterest KtLint](https://pinterest.github.io/ktlint)
- [Android Kotlin Style Guide](https://developer.android.com/kotlin/style-guide)
- [Code Review Expert](../android-code-review-expert/SKILL.md)
