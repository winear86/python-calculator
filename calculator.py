#!/usr/bin/env python3
"""
Simple Interactive Calculator
=============================

A clean, beginner-friendly calculator built while learning Python.
Demonstrates classes, error handling, input validation, and basic OOP.

Features:
- Basic arithmetic (+, -, *, /, ** power, % modulo)
- Parentheses support
- Calculation history
- Memory functions (M+, M-, MR, MC)
- Graceful error handling

Author: winear86
Created as a learning project
"""

import operator
from typing import Optional, Union


class Calculator:
    """A simple calculator with history and memory support."""

    def __init__(self):
        self.history: list[str] = []
        self.memory: float = 0.0

    def calculate(self, expression: str) -> Union[float, str]:
        """
        Safely evaluate a mathematical expression.
        Returns the result or an error message.
        """
        # Allowed characters (basic safety check)
        allowed = set("0123456789.+-*/()% ")
        cleaned = expression.replace("**", "*")
        if not all(c in allowed for c in cleaned):
            return "Error: Invalid characters in expression"

        try:
            # Evaluate with restricted environment for safety
            result = eval(expression, {"__builtins__": {}}, {})
            if isinstance(result, (int, float)):
                # Store successful calculation in history
                self.history.append(f"{expression} = {result}")
                return result
            return "Error: Invalid result"
        except ZeroDivisionError:
            return "Error: Division by zero"
        except SyntaxError:
            return "Error: Invalid syntax"
        except Exception:
            return "Error: Could not evaluate expression"

    def memory_add(self, value: float) -> None:
        """Add a value to memory (M+)."""
        self.memory += value

    def memory_subtract(self, value: float) -> None:
        """Subtract a value from memory (M-)."""
        self.memory -= value

    def memory_recall(self) -> float:
        """Recall the value stored in memory (MR)."""
        return self.memory

    def memory_clear(self) -> None:
        """Clear memory (MC)."""
        self.memory = 0.0

    def show_history(self) -> None:
        """Display calculation history."""
        if not self.history:
            print("No calculations yet.")
            return
        print("\n--- History ---")
        for entry in self.history[-10:]:  # Show last 10
            print(entry)
        print("---------------\n")


def main():
    """Main interactive loop."""
    calc = Calculator()

    print("=" * 40)
    print("   Python Calculator  (Learning Project)")
    print("=" * 40)
    print("Operations: +  -  *  /  **  %   (use parentheses)")
    print("Commands:")
    print("  history  → show recent calculations")
    print("  m+       → add last result to memory")
    print("  m-       → subtract last result from memory")
    print("  mr       → recall memory")
    print("  mc       → clear memory")
    print("  q / quit → exit")
    print("-" * 40)

    last_result: Optional[float] = None

    while True:
        try:
            user_input = input("calc> ").strip()

            if not user_input:
                continue

            cmd = user_input.lower()

            if cmd in ("q", "quit", "exit"):
                print("Goodbye! Keep learning 🚀")
                break

            if cmd == "history":
                calc.show_history()
                continue

            if cmd == "mr":
                print(f"Memory: {calc.memory_recall()}\n")
                continue

            if cmd == "mc":
                calc.memory_clear()
                print("Memory cleared.\n")
                continue

            if cmd == "m+" and last_result is not None:
                calc.memory_add(last_result)
                print(f"Added {last_result} to memory. Memory = {calc.memory}\n")
                continue

            if cmd == "m-" and last_result is not None:
                calc.memory_subtract(last_result)
                print(f"Subtracted {last_result} from memory. Memory = {calc.memory}\n")
                continue

            # Normal calculation
            result = calc.calculate(user_input)

            if isinstance(result, (int, float)):
                last_result = float(result)
                print(f"= {result}\n")
            else:
                print(f"{result}\n")

        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except EOFError:
            break


if __name__ == "__main__":
    main()
