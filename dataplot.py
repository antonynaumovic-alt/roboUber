import matplotlib.pyplot as plt
import copy

def plotTaxiAccount(accounts, taxiAmount, dispatcherAccounts):

    iter1 = 0 #Current Taxi

    totalRevenue = copy.deepcopy(dispatcherAccounts)


    legendNames = []
    for taxiNum in range(taxiAmount):
        plt.plot(accounts[iter1])
        legendNames.append(f"Taxi {iter1+1}")
        for i in range(len(totalRevenue)):
            totalRevenue[i] += accounts[iter1][i]
        iter1 += 1


    totalAccounts = copy.deepcopy(totalRevenue)
    for i in range(len(totalRevenue)):
        totalRevenue[i] -= 256*taxiAmount

    legendNames.append("Dispatcher")
    legendNames.append("Revenue")
    legendNames.append("Accounts")
    plt.plot(dispatcherAccounts)
    plt.plot(totalRevenue)
    plt.plot(totalAccounts)

    plt.title("Taxi Accounts Over Runtime")
    plt.xlabel("Time (Minutes)")
    plt.ylabel("Account Balance")
    plt.axhline(y=0, color='black', linestyle=':')
    plt.legend(legendNames)
    plt.savefig('taxiStats.png', bbox_inches='tight')
    plt.show()
