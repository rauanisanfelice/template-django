#!/usr/bin/env python3
import json, os

FILE_COVERAGE = "././app/coverage.json"
COVERAGE_PERCENTAGE = os.environ.get("COVERAGE_PERCENTUAL", None)

try:
    with open(FILE_COVERAGE) as coverage_file:
        data = json.load(coverage_file)

except FileNotFoundError:
    raise

if COVERAGE_PERCENTAGE is None:
    raise Exception("COVERAGE_PERCENTUAL variavel não declarada")

percentual = int(data["totals"]["percent_covered"])
print(f"Lines Convered: {data['totals']['covered_lines']}")
print(f"Lines Faltantes: {data['totals']['missing_lines']}")
print(f"Lines Excluidas: {data['totals']['excluded_lines']}", end="\n\n")
print(f"Percent Accept Convered: {COVERAGE_PERCENTAGE}%")
print(f"Percent Current Convered: {percentual}%", end="\n\n")

if percentual > int(COVERAGE_PERCENTAGE):
    print("Tests passed!")
else:
    raise Exception(
        f"Percentual de cobertura {percentual}% é menor que o limite de {COVERAGE_PERCENTAGE}%"
    )
