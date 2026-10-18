import argparse
import json
import sys
import os

# src klasörünün import edilebilmesi için sistem yoluna ekle
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from engine import calculate_anova_apriori

def main():
    parser = argparse.ArgumentParser(description="G*Power ANOVA CLI Clone")
    parser.add_argument("--test", type=str, required=True)
    parser.add_argument("--mode", type=str, required=True)
    parser.add_argument("--f", type=float, required=True)
    parser.add_argument("--alpha", type=float, required=True)
    parser.add_argument("--power", type=float, required=True)
    parser.add_argument("--groups", type=int, default=3)

    args = parser.parse_args()

    if args.test == "anova-oneway" and args.mode == "a-priori":
        res = calculate_anova_apriori(args.alpha, args.power, args.f, args.groups)
        print(json.dumps(res))
    else:
        print(json.dumps({"error": "Unsupported test or mode"}))
        sys.exit(1)

if __name__ == "__main__":
    main()