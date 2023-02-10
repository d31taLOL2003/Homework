import library


def run_control_function() -> str:
    amount = library.get_number("Введіть суму, яку потрібно внести: ")
    hryvnia, kopiyka = library.hryvnia_kopiyka(amount)
    return f"Сума, яку ви надали: {hryvnia} {kopiyka}"


if __name__ == "__main__":
    print(run_control_function())
