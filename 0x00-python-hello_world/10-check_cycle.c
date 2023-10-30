#include "lists.h"

int check_cycle(listint_t *list)
{
    listint_t* bunny = list;
    listint_t* turtle = list;

    while (bunny != NULL && turtle != NULL && bunny->next != NULL)
    {
        bunny = bunny->next->next;
        turtle = turtle->next;

        if (turtle == bunny)
            return (1);

    }
    return (0);
}
