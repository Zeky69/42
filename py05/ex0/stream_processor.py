#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, List, Union


class DataProcessor(ABC):

    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):

    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        return isinstance(data, list) and all(
            isinstance(x, (int, float)) for x in data)

    def process(self, data: List) -> str:
        try:
            if not data:
                return "No data provided"

            count: int = len(data)
            total: Union[int, float] = sum(data)
            avg: float = total / count

            return f"Processed {count} numeric values, sum={total}, \
avg={avg:.1f}"
        except Exception as e:
            return f"Error processing numeric data: {e}"


class TextProcessor(DataProcessor):

    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        return isinstance(data, str)

    def process(self, data: str) -> str:
        try:
            char_count: int = len(data)
            word_count: int = len(data.split())
            return f"Processed text: {char_count} characters, \
{word_count} words"
        except Exception as e:
            return f"Error processing text data: {e}"


class LogProcessor(DataProcessor):

    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        return isinstance(data, str) and (":" in data)

    def process(self, data: Any) -> str:
        try:
            parts: List[str] = data.split(":", 1)
            level: str = parts[0].strip()
            message: str = parts[1].strip()

            tag: str = "[INFO]"
            if "ERROR" in level:
                tag = "[ALERT]"
            elif "WARNING" in level:
                tag = "[WARN]"

            return f"{tag} {level} level detected: {message}"
        except Exception as e:
            return f"Error processing log data: {e}"


def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
    print()
    print("Initializing Numeric Processor...")
    num_proc = NumericProcessor()
    data = [1, 2, 3, 4, 5]
    print(f"Processing data: {data}")
    if num_proc.validate(data):
        print("Validation: Numeric data verified")
        print(num_proc.format_output(num_proc.process(data)))

    print()
    print("Initializing Text Processor...")
    text_proc = TextProcessor()
    data = "Hello Nexus World"
    print(f"Processing data: \"{data}\"")
    if text_proc.validate(data):
        print("Validation: Text data verified")
        print(text_proc.format_output(text_proc.process(data)))
    print()
    print("Initializing Log Processor...")
    log = LogProcessor()
    data = "ERROR: Connection timeout"
    print(f"Processing data: \"{data}\"")
    if log.validate(data):
        print("Validation: Log entry verified")
        print(log.format_output(log.process(data)))
    print()
    print("=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")

    stream_data = [
        (num_proc, [1, 2, 3]),
        (text_proc, "Hello Python"),
        (log, "INFO: System ready")
    ]

    counter = 1
    for processor, data in stream_data:
        result = processor.process(data)
        print(f"Result {counter}: {result}")
        counter += 1

    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
