---
name: explain-this-file
description: Explains the purpose and contents of a file in simple, easy-to-understand language
argument-hint: [filepath]
disable-model-invocation: true
---

Explain the following file in simple, easy-to-understand language. Focus on:
- What the file does
- Its main purpose
- Key components or sections
- How it fits into the larger system

Avoid technical jargon. Make it accessible to someone unfamiliar with the codebase.

File to explain: $0

!`cat $0`