# Training Design Principles: AI-Native Developer Edition

## Positioning Statement
This training is not a Foundry API crash course and not a generic AI-pair programming class. It is a Foundry capability mastery course for AI-native developers.

## Principle 1: Teach Decisions, Not APIs
If ChatGPT can explain a field or generate boilerplate, class time should not be spent on it. Class time is for platform selection, boundaries, cost, risk, and production consequences.

## Principle 2: Prioritize What AI Does Not Know
The instructor brings current API drift, portal reality, upstream workshop bugs, cost constraints, and business-context judgment.

## Principle 3: Every Exercise Produces a Prompt Spec
The reusable artifact is not just code. It is the spec that lets a team repeatedly ask AI for correct implementation under explicit constraints.

## Principle 4: Negative Examples Must Be Explicit
AI mistakes are often syntactically valid and semantically wrong. Each module must name the likely wrong outputs and how to catch them.

## Principle 5: Red-Team, Portability, Scaling, and Cost Are Required
These are not Day-3 polish. They shape architecture decisions from Day 1 and appear in the capstone rubric.

## Role Split
| Role | Does | Does not do |
|------|------|-------------|
| Instructor | Explains decisions, blind spots, and review criteria | Dictates API field usage |
| Learner | Writes specs, asks AI to implement, verifies output | Copies boilerplate by hand |
| AI assistant | Generates code and explains APIs | Owns architecture decisions |
