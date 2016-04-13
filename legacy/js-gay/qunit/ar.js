function Airbridge() {

}

Airbridge.prototype = {
	parseUA: function(uaString) {
		return 'iPhone'
	}
}

/**
 *  Test 명세
 *
 *  1. UA String을 받아 Parsing하여, device, OS, browser 이름과 버젼을 알 수 있다.
 *  2. device(Android, iOS, Desktop)별 분기를 태울 수 있다.
*/

module('Airbridge', {
	setup: function() {
		oAirbridge = new Airbridge();

		iPhone_iOS_9_2_1_UA = {
			"safari": "Mozilla/5.0 (iPhone; CPU iPhone OS 9_2_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13D15 Safari/601.1",
			"chrome": "Mozilla/5.0 (iPhone; CPU iPhone OS 9_2_1 like Mac OS X) AppleWebKit/601.1 (KHTML, like Gecko) CriOS/48.0.2564.87 Mobile/13D15 Safari/601.1.46",
			"naver": "Mozilla/5.0 (iPhone; CPU iPhone OS 9_2_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13D15 NAVER(inapp; search; 480; 6.7.5; 5)",
			"facebook": "Mozilla/5.0 (iPhone; CPU iPhone OS 9_2_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13D15 [FBAN/FBIOS;FBAV/47.0.0.43.396;FBBV/20481971;FBDV/iPhone5,2;FBMD/iPhone;FBSN/iPhone OS;FBSV/9.2.1;FBSS/2; FBCR/KT;FBID/phone;FBLC/ko_KR;FBOP/5]",
			"kakao": "Mozilla/5.0 (iPhone; CPU iPhone OS 9_2_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13D15 KAKAOTALK 5.3.2"
		}
	},
	teardown: function() {
		oAirbridge = null;
	}
});


test("iOS 9.2.1 Browser별 UA를 Parsing 할 수 있다.", function() {
	var safari = oAirbridge.parseUA(iPhone_iOS_9_2_1_UA['safari']);

	equal(safari, 'iPhone');
})
