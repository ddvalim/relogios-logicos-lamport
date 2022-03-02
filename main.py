from random import randint
from proccess import Proccess


def main():
    proccesses = [
        Proccess(0, 4),
        Proccess(1, 4),
        Proccess(2, 4),
        Proccess(3, 4)
    ]

    n_events = 6
    n_proccess = 4
    counter = 0

    while counter <= n_events:
        p_send = randint(0, (n_proccess - 1))
        p_receive = randint(0, (n_proccess - 1))

        print('\n--!------!--')
        print(f'Proccess sending message: {p_send}')
        print(f'Proccess receiving message: {p_receive}')

        if (p_send == p_receive):
            clock_value = proccesses[p_send].get_clock()[p_send]

            proccesses[p_send].set_clock(p_send, clock_value+1)

            curr_proccess_clock = proccesses[p_send].get_clock()

            print('\n Internal Event')
            print(f'Current Proccess Clock: {curr_proccess_clock}')
            print('--!------!--')
        else:
            p_send_clock_value = proccesses[p_send].get_clock()[p_send]

            proccesses[p_send].set_clock(p_send, p_send_clock_value + 1)

            p_send_clock = proccesses[p_send].get_clock()

            p_receive_clock = proccesses[p_receive].get_clock()

            for i in range(len(p_receive_clock)):
                if i == p_receive:
                    p_receive_clock_value = proccesses[p_send].get_clock()[p_receive]
                    proccesses[p_receive].set_clock(p_receive, p_receive_clock_value + 1)
                else:
                    clock_value = max(p_receive_clock[i], p_send_clock[i])
                    proccesses[p_receive].set_clock(i, clock_value)

            print('\n--!------!--')
            print('Message Sending Event')
            print(f'\n Proccess which has sent message clock: {p_send_clock}')
            print(
                f'Proccess which has received message clock: {p_receive_clock}')

        counter += 1

    print('--!-- End of Algorithm --!--')


main()
