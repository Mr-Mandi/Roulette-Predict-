import logging
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

logger = logging.getLogger(__name__)

def get_graph (
        list_game_numbers : list,
        balance_record : list
    ) -> None :
    fig, ax = plt.subplots()  # Create a figure containing a single axes.
    ax.plot(list_game_numbers, balance_record)  # Plot some data on the axes.  
    ax.set_ylabel('Balance')
    ax.set_xlabel('Game Number')
    plt.show()


def main() -> bool :  
    """
        =======================================================================================================================================================
        plays = np.array()
        If the matrix has more than 2 dimensions, I take the dimensions as sections of the rule, example 1-18, 1 and 12, that is, if you win, the result is * 2
        
        If the matrix is a single dimension, each number is a token, that is, if it is correct, it is 1 * 35
        
        =======================================================================================================================================================
        Returns:
            bool: If no error occurs when executing the response is True
    """
    
    games_number = input("Enter count of plays: ") 
    token_value = input("Enter token value: ")
    balance = input("Enter you Balance: ")
    
    try :
        games_number = int(games_number)
        token_value = float(token_value)
        balance = float(balance)
    except ValueError:
        logger.error("Enter a Valid Number")
        return False
    
    # array par
    plays = np.array([
        [1, 2, 3, 4 , 5, 6 ,7 , 8, 9, 10, 11, 12] , 
        [25,26,27,28,29,30,31,32,33,34,35,36]
        ]
    )
    
    # plays = np.array(
    #     [0, 1, 3, 4 , 5, 6 ,7 , 8, 9, 11, 12 , 16 , 17, 18, 19, 20 , 21, 22, 23, 24, 25,28,29,30,31,33,34,35,36] , 
    # )
    
    if plays.ndim == 0 :
        logger.error("plays >= 1")
        return False
    
    if plays.size > 30 :
        logger.error("number plays invalid > 30")
        return False    
    
    
    list_game_numbers : list = []
    balance_record  : list = []
    
    list_game_numbers.append(0)
    balance_record.append(balance)
    

    for _item in range(1 , games_number + 1):
        number_random = np.random.randint(0,36)
        if plays.ndim == 1 :
            if number_random in plays :
                result = ( (token_value * 35) -  (plays.size - 1)  * token_value ) * 0.97
                balance += result
            else :
                if balance < (plays.size * token_value)  :
                    balance = 0
                    break
                result = ( plays.size * token_value)
                balance -= result
        else :
            for item , play in enumerate(plays) :
                if number_random in play :
                    result = ( (token_value * 2) -  (plays.shape[0] - 1)  * token_value ) * 0.97
                    balance += result
                else :
                    result = (plays.shape[0] - 1) * token_value
                    if balance < result :
                        balance = 0
                        break
                    balance -= result

        list_game_numbers.append(_item)
        balance_record.append(balance)
    
    print("Balance End: ", balance)
    get_graph(
        list_game_numbers,
        balance_record
    )
    
    return True


if __name__ == '__main__':
    print(
        """
            #####################################
            #####################################
                Only Play by Token o Sections
            #####################################
            #####################################
        """, end="\n\n"
    )
    status = main()
    print("success" if status == True else "failure")