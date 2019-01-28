#include <stdio.h>

/**
 * Finds max number that is divisible by power but
 * less than or equal to num.
 * @return max number or 0 if err
 */
int max_pow_num(int power, int num)
{
    if (power < 1)
        return 0;

    int res = 1;
    while (res * power <= num)
        res *= power;

    return num > 0 ? res : 0;
}

int solve_Josephus_problem(int n_people)
{
    int step = 2;
    return (n_people - max_pow_num(step, n_people)) * step + 1;
}

int main()
{
    int n_people;
    printf("Input amount of people: ");
    scanf("%d", &n_people);
    printf("Winning position is: %d", solve_Josephus_problem(n_people));
    return 0;
}
