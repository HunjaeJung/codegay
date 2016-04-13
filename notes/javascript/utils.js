var utils = {
    capitalizeFirstLetter: function(string) {
        /**
         *  텍스트의 첫번째 문자를 대문자로 바꿉니다.
        */
        return string.charAt(0).toUpperCase() + string.slice(1);
    },

    camelCaseToUnderScore: function (text) {
        /**
         *  camelCase를under_score로 바꿔줍니다.
        */
        return text.replace(/(?:^|\.?)([A-Z])/g, function (x,y){return "_" + y.toLowerCase()}).replace(/^_/, "")
    }

}
