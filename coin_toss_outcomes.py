
outcomes = ['H', 'T']

def combine_outcomes(layers):
    result_rows = []
    for r in outcomes:
        row = ''
        if layers == 1:
            row += r
            result_rows.append(row)
        else:
            sub_rows= combine_outcomes(layers-1)
            for line in sub_rows:
                row = r + line
                result_rows.append(row)
    return result_rows


def main():
    c = combine_outcomes(6)
    print(len(c))
    for i in c:
        print(i)


if __name__ == '__main__':
    main()
