bool isPalindrome(int x) {
    if(x < 0 ) {
        return false;
    }
    int y = x ;
    long reserved = 0 ;
    while(y != 0){
        int z = y % 10;
        y = y / 10;
        reserved = (reserved * 10) + z;
    }
    if(reserved == x) {
         return true ;
    }
    else {
        return false ;
    }
       
    
}