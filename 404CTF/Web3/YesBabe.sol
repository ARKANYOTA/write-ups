pragma solidity ^0.4.6;

// SPDX-License-Identifier: MIT

contract FreeMoney {
    function getMoney(uint256 numTokens) public ;
    function reset() public ;
    function transfer(address receiver, uint256 numTokens) public returns (bool);
    function enterHallebarde() public;
    function getMembershipStatus(address memberAddress) external view returns (bool);
}

contract YesBabe {
    address counterAddr;

    function setCounterAddr(address _counter) public payable {
       counterAddr = _counter;
    }

    function resait() external {
        FreeMoney(counterAddr).reset();
    }

    function larjen() external {
        FreeMoney(counterAddr).getMoney(10);
    }

    function transfair() external returns (bool) {
        return FreeMoney(counterAddr).transfer(0xE37389059DcE67c0cDDaad765949dcc059679640, 15); // Ici l'adresse du créateur du contrat (j'avais pas trop d'idée)
    }


    function enterBabe() external {  
        FreeMoney(counterAddr).enterHallebarde();
    }

    function taist(address testAddr) external returns (bool) {
        return FreeMoney(counterAddr).getMembershipStatus(testAddr);
    }
}
