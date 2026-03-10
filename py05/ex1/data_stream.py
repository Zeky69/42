#!/usr/bin/env python3

import abc
from typing import Any, List, Dict, Union, Optional


class DataStream(abc.ABC):

    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id
        self.processed_count = 0

    @abc.abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        return [item for item in data_batch if item is not None]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "type": self.__class__.__name__,
            "processed": self.processed_count
        }


class SensorStream(DataStream):

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            valid_data = [
                d for d in data_batch
                if isinstance(d, str) and ":" in d
            ]

            if not valid_data:
                return "No valid sensor data found"

            temps = []

            for item in valid_data:
                key, val = item.split(":")
                if key.strip() == "temp":
                    temps.append(float(val))

            self.processed_count += len(valid_data)

            avg_temp = sum(temps) / len(temps) if temps else 0.0
            return (
                f"Sensor analysis: {len(valid_data)} readings processed, "
                f"avg temp: {avg_temp} °C"
            )

        except ValueError as e:
            return f"Sensor processing error: {e}"
        except Exception as e:
            return f"Critical sensor failure: {e}"

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria == "critical":
            return [
                d for d in data_batch
                if isinstance(d, str) and "alert" in d
            ]
        return super().filter_data(data_batch)


class TransactionStream(DataStream):

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            valid_ops = [
                d for d in data_batch
                if isinstance(d, str) and ":" in d
            ]

            net_flow = 0

            for op in valid_ops:
                action, amount = op.split(":")
                val = int(amount)

                if action.strip() == "buy":
                    net_flow += val
                elif action.strip() == "sell":
                    net_flow -= val

            self.processed_count += len(valid_ops)
            sign = "+" if net_flow >= 0 else ""
            return (
                f"Transaction analysis: {len(valid_ops)} operations, "
                f"net flow: {sign}{net_flow} units"
            )

        except Exception as e:
            return f"Transaction processing error: {e}"

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria == "high_value":
            return [
                d for d in data_batch
                if isinstance(d, str) and int(d.split(":")[1]) > 100
            ]
        return super().filter_data(data_batch)


class EventStream(DataStream):

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            valid_events = [e for e in data_batch if isinstance(e, str)]

            error_count = 0
            for event in valid_events:
                if "error" in event.lower():
                    error_count += 1

            self.processed_count += len(valid_events)
            return (
                f"Event analysis: {len(valid_events)} events, "
                f"{error_count} error detected"
            )

        except Exception as e:
            return f"Event processing error: {e}"


class StreamProcessor:

    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        self.streams.append(stream)

    def process_all(self, data_map: Dict[str, List[Any]]) -> None:
        print("Processing mixed stream types through unified interface...")

        results = []
        for stream in self.streams:
            if stream.stream_id in data_map:
                data = data_map[stream.stream_id]

                stream.process_batch(data)

                count = stream.get_stats()['processed']
                type_name = "Sensor"
                unit = "readings"

                if isinstance(stream, TransactionStream):
                    type_name = "Transaction"
                    unit = "operations"
                elif isinstance(stream, EventStream):
                    type_name = "Event"
                    unit = "events"

                results.append(
                    f"- {type_name} data: {count} {unit} processed"
                )

        print("Batch 1 Results:")
        for res in results:
            print(res)


def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

    print("\nInitializing Sensor Stream...")
    sensor_stream = SensorStream("SENSOR_001")
    print(f"Stream ID: {sensor_stream.stream_id}, Type: Environmental Data")

    sensor_data = ["temp:22.5", "humidity:65", "pressure:1013"]
    print(f"Processing sensor batch: {sensor_data}")
    print(sensor_stream.process_batch(sensor_data))

    print("\nInitializing Transaction Stream...")
    trans_stream = TransactionStream("TRANS_001")
    print(f"Stream ID: {trans_stream.stream_id}, Type: Financial Data")

    trans_data = ["buy:100", "sell:150", "buy:75"]
    print(f"Processing transaction batch: {trans_data}")
    print(trans_stream.process_batch(trans_data))

    print("\nInitializing Event Stream...")
    event_stream = EventStream("EVENT_001")
    print(f"Stream ID: {event_stream.stream_id}, Type: System Events")

    event_data = ["login", "error", "logout"]
    print(f"Processing event batch: {event_data}")
    print(event_stream.process_batch(event_data))

    print("\n=== Polymorphic Stream Processing ===")

    processor = StreamProcessor()
    processor.add_stream(sensor_stream)
    processor.add_stream(trans_stream)
    processor.add_stream(event_stream)

    sensor_stream.processed_count = 0
    trans_stream.processed_count = 0
    event_stream.processed_count = 0

    mixed_data = {
        "SENSOR_001": ["temp:22.5", "temp:24.0"],
        "TRANS_001": ["buy:100", "buy:200", "sell:50", "buy:20"],
        "EVENT_001": ["login", "click", "logout"]
    }

    processor.process_all(mixed_data)

    print("\nStream filtering active: High-priority data only")

    crit_sensors = ["alert:fire", "alert:leak", "temp:50"]
    filtered_sensors = sensor_stream.filter_data(crit_sensors, "critical")

    large_trans = ["buy:500", "sell:50"]
    filtered_trans = trans_stream.filter_data(large_trans, "high_value")

    print(
        f"Filtered results: {len(filtered_sensors)} critical sensor alerts, "
        f"{len(filtered_trans)} large transaction"
    )

    print("All streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
