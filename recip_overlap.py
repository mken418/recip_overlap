#!/usr/bin/env python3

def recip_overlap(X1, X2, Y1, Y2, thresh):
    """
    Will determine reciprocal overlap for two ranges.
    Threshold (between 0 and 1) is how much of an overlap is required for the event to be considered the same.
    X1 to X2 is the start to stop for the first range.
    Y1 to Y2 is the start to stop for the second range.
    """

    
    if max(X1, Y1) <= min(X2, Y2): #there is overlap
        #check if they are the same
        """
        X1----------X2
        Y1----------Y2
        """
        if X1 == Y1 and X2 == Y2:
            print('X1----------X2\nY1----------Y2')
            return True


        #check if Y range is completely within X
        """
        X1-------------X2
            Y1------Y2
        """
        if Y2 <= X2 and Y1 >= X1:
            print('X1-------------X2\n    Y1------Y2    ')
            overlap = (Y2 - Y1) / (X2 - X1)
            if overlap >= thresh:
                return True
            else:
                return False


        #check if Y range starts in X and ends after X
        """
        X1-------------X2
            Y1--------------------------Y2
             -----------
             b
        ---
        a
                         ----------------
                         c
        """
        if Y2 >= X2 and Y1 >= X1:
            print('X1-------------X2\n    Y1--------------------------Y2')
            b = X2-Y1
            a = Y1-X1
            c = Y2-X2
            if b/(a+b) >= thresh and b/(b+c) >= thresh:
                return True
            else:
                return False 

       

        #check if X range starts in Y range and ends after Y
        """
             X1---------------------------------X2
        Y1-----------------Y2

        ------
        a
             ---------------
             b
                            --------------------
                            c
        """
        if Y2 <= X2 and Y1 <= X1:
            print('     X1---------------------------------X2\nY1-----------------Y2')
            b = Y2-X1
            a = X1-Y1
            c = X2-Y2
            if b/(a+b) >= thresh and b/(b+c) >= thresh:
                return True
            else:
                return False

        
        #check if X range is completely within Y
        """
                X1----------X2
        Y1-------------------------------Y2
        """
        if Y2 >= X2 and Y1 <= X1:
            print('        X1----------X2\nY1-------------------------------Y2')
            overlap = (X2-X1) / (Y2-Y1)
            if overlap >= thresh:
                return True
            else:
                return False
            
    #no overlap at all  
    else:
        return False

