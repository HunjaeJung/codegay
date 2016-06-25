function VendingMachine() {};

VendingMachine.prototype = {

    buy : function(sBeverage){
        return sBeverage;
    }
}


var oVendingMachine = null;

module('VendingMachine', {
    setup : function(){
        oVendingMachine = new VendingMachine();
    },
    teardown : function(){
        /* 리소스 정리 */
        oVendingMachine = null;
    }
});

test("자판기에서 음료를 뽑을 수 있다.", function(){
	// Given
	// When
    var sBeverage = oVendingMachine.buy("Coke");

	// Then
    equal(sBeverage, "Coke");
});

test("자판기에서 사이다를 뽑을 수 있다.", function(){
    // Given
    // When
    var sBeverage1 = oVendingMachine.buy("Sprite");

    // Then
    equal(sBeverage1, "Sprite");
});



test("자판기에서 원하는 음료를 뽑을 수 있다.", function(){
    // Given
    // When
    var sBeverage1 = oVendingMachine.buy("Sprite");
    var sBeverage2 = oVendingMachine.buy("Orange Juice");
    var sBeverage3 = oVendingMachine.buy("Apple Juice");

    // Then
    equal(sBeverage1, "Sprite");
    equal(sBeverage2, "Orange Juice");
    equal(sBeverage3, "Apple Juice");
});

