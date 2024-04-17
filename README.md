# Pythonic 1 Billion Row Challenge

This mini-project is a personal challenge in optimization problems. The
challenge is adapted from its
[original form](https://www.morling.dev/blog/one-billion-row-challenge/) (in
Java) by [Gunnar Morling](https://github.com/gunnarmorling).

The premise is simple - In `/data/`, a sample of ~44,000 weather stations exist.
From this initial data, 1 billion rows of a CSV are created of the following
sample structure:

```
Hamburg;12.0
Bulawayo;8.9
Palembang;38.8
St. John's;15.2
Cracow;12.6
...
```

The program should save and return the minimum, mean, and maximal values per
station, ordered alphabetically. For simplicity's sake, I've created generation
functions as well as standardized the output to CSV for comparison.

**Notably,** and due to testing the timing, I've opted to significantly reduce
the problem size to a paltry 100 million data points. This reduces the time
requirements for each iteration and allows me to test timings much faster.

## Running

The project is limited to standard libraries within Python 3.12, so that is the
major requirement. The project also uses progress bars from `alive_progress`, so
`pip install alive-progress` is also required.

To generate the 1 billion rows, simply run `py buildGeneratedRows.py`.

Each individual script contains a different attempt at constructing the
generated data, so you can run them individually to generate a CSV file in the
`out` folder. Each individual script generates a separate CSV file, for
comparison's sake.

# License TL;DR

This project is distributed under the MIT license. This is a paraphrasing of a
[short summary](https://tldrlegal.com/license/mit-license).

This license is a short, permissive software license. Basically, you can do
whatever you want with this software, as long as you include the original
copyright and license notice in any copy of this software/source.

## What you CAN do:

-   You may commercially use this project in any way, and profit off it or the
    code included in any way;
-   You may modify or make changes to this project in any way;
-   You may distribute this project, the compiled code, or its source in any
    way;
-   You may incorporate this work into something that has a more restrictive
    license in any way;
-   And you may use the work for private use.

## What you CANNOT do:

-   You may not hold me (the author) liable for anything that happens to this
    code as well as anything that this code accomplishes. The work is provided
    as-is.

## What you MUST do:

-   You must include the copyright notice in all copies or substantial uses of
    the work;
-   You must include the license notice in all copies or substantial uses of the
    work.

If you're feeling generous, give credit to me somewhere in your projects.
