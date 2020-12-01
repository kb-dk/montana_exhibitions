window.changeLanguage = (function (window, $, undefined) {
    var minutesBeforeReset = 4.9,
        cookieName = 'lang',
        filePostfixEn = 'Uk';

    var ChangeLanguage = function(minutesBeforeReset, cookieName) {
        this.cookieExpirationMs = Math.round(minutesBeforeReset * 1000 * 60);
        this.cookieName = cookieName;
    }

    ChangeLanguage.prototype = {
        setLangCookie : function (langStr) {
            var expire = new Date();
            expire.setTime(expire.getTime() + this.cookieExpirationMs);
            document.cookie = changeLanguage.cookieName + '=' + langStr + '; expires=' + expire + '; path=/';
        },
        resetLangCookie : function () {
            var expire = new Date('1971-01-01');
            document.cookie = changeLanguage.cookieName + '=; expires=' + expire + '; path=/';
        },
        getLangFromCookie : function () {
            var that = this,
                cookies = document.cookie.split(';'),
                lang = ''
                result = cookies.filter(function (cookie) {
                    return cookie.split('=')[0] === that.cookieName;
                });
            return result.length ? result[0].split('=')[1] : 'da'; // Defaults to 'da'
        },
        getLangFromFileName : function () {
            var tmpFileName = location.pathname;
            if (tmpFileName === '/') {
                tmpFileName = '/index.html';
            }
            var lastTwoLetters = tmpFileName.substr(tmpFileName.lastIndexOf('.') - 2, 2);
            if (lastTwoLetters === filePostfixEn) {
                return 'en';
            }
            return 'da';
        },
        getFileNameI18ned : function (langStr) {
            var tmpFileName = location.pathname,
                lastTwoLetters = tmpFileName.substr(tmpFileName.lastIndexOf('.') - 2, 2);
            if ((langStr === 'en' && lastTwoLetters === filePostfixEn) || (langStr === 'da' && lastTwoLetters !== filePostfixEn)) {
                return tmpFileName;
            } else {
                if (langStr !== 'da') {
                    return tmpFileName.slice(0, tmpFileName.lastIndexOf('.')) + filePostfixEn + tmpFileName.slice(tmpFileName.lastIndexOf('.'));
                } else {
                    return tmpFileName.slice(0, tmpFileName.lastIndexOf('.') - 2) + tmpFileName.slice(tmpFileName.lastIndexOf('.'));
                }
            }
        }
    }

    return new ChangeLanguage(minutesBeforeReset, cookieName);
})(window, jQuery);

if (changeLanguage.getFileNameI18ned('da').indexOf('/index.html') >= 0) {
    if (changeLanguage.getLangFromFileName() !== changeLanguage.getLangFromCookie()) {
        location.href = changeLanguage.getFileNameI18ned(changeLanguage.getLangFromCookie());
    }
}
// For some reason the cookies does not seem to invalidate even though their expiration has come? So now we force resets the language cookie after 4.5 minuttes from load
changeLanguage.timer = setTimeout(changeLanguage.resetLangCookie, changeLanguage.cookieExpirationMs);

$(document).ready(function() {
    $('#da').click(function (e) {
        changeLanguage.setLangCookie('da');
    });

    $('#en').click(function (e){
        changeLanguage.setLangCookie('en');
    });
});
