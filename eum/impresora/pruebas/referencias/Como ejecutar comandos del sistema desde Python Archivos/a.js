(function() {
    var dc = {};
    var gu = "2DE7B66B7E5D79591F4389B002D1541D"
    String.prototype.dts_hash_code=function(){var hash=0;if(this.length==0)return hash;for(i=0;i<this.length;i++){char=this.charCodeAt(i);hash=((hash<<5)-hash)+char;hash=hash&hash}return hash;};

    function _dtsi() {
        a = document.createElement("a"), a.href = window.location.href, _dts.host = a.hostname, "undefined" != typeof document.referrer && document.referrer.length > 0 ? (_dts.r = document.referrer, _dts.p = _dts_gp(_dts.r), "q" in _dts.p ? _dts.q = _dts.p.q : "query" in _dts.p ? _dts.q = _dts.p.query : "p" in _dts.p ? _dts.q = _dts.p.p : "text" in _dts.p ? _dts.q = _dts.p.text : "wd" in _dts.p ? _dts.q = _dts.p.wd : _dts.q = 0) : (_dts.r = 0, _dts.q = 0)
    }
    var _dts = {};
    _dtsi();

    function __dtsinit() {
        var c = document.cookie.split(';');
        for(i = c.length - 1; i >= 0; i--) {
           cv = c[i].trim().split('=');
           dc[cv[0]] = cv[1];
        }
    }
    var di = __dtsinit();

    if(gu !== false && gu.length > 15) {
        lp(gu);
    } else if("__dtsu" in dc && dc.__dtsu.length > 15) {
        lp(dc.__dtsu);
    } else {
        window.addEventListener('message', function(e) {
            if(e.origin.indexOf('dtscout.com') >= 0) {
                if(e.data.length > 0) {
                    var temp = JSON.parse(e.data);
                    lp(temp.u);
                }
            }
        });

        var i = document.createElement('iframe');
        i.src = "//t.dtscout.com/idg/";
        i.width = 0;
        i.height = 0;
        i.style.display = 'none';
        document.body.appendChild(i);
    }

    function lp(data) {
        var uid = data;
        __sc('__dtsu', uid, 800);
        (function(){var t,n=[];document.title&&document.title.length>0&&n.push("phint=__bk_t%3D"+encodeURIComponent(document.title));var o=document.getElementsByTagName("meta");if(o)for(t=0;t<o.length;t++)if("keywords"==o[t].name.toLowerCase()){n.push("phint=__bk_k%3D"+encodeURIComponent(o[t].content));break}window.location.href&&n.push("phint=__bk_l%3D"+encodeURIComponent(window.location.href)),n.push("r="+Math.floor(99999999*Math.random())),t=document.createElement("img"),t.width=0,t.height=0,t.style.visibility="hidden",t.src="//tags.bluekai.com/site/27675?id="+uid+"&ret=html&"+n.join("&"),document.getElementsByTagName("body")[0].appendChild(t);t.onload=function(e){if(e.target){try{e.target.parentNode.removeChild(e.target);}catch(e){}}}})();(function(){var s=document.createElement("script");s.src="https://n-cdn.areyouahuman.com/play/ZQp6LCe0OO3LeZB6ES1CZrJvMefQTtT9oZjddBS5?AYAH_P2="+uid+"&AYAH_F1=Lotame";s.async=true;document.getElementsByTagName("body")[0].appendChild(s);})();    }

    function _dts_gp(t) {
        var d = {},
            e = t.split("?", 2);
        if (2 == e.length) {
            e = e[1].split("&");
            for (var s = 0; s < e.length; s++) {
                var _ = e[s].split("=", 2);
                2 == _.length && (d[_[0]] = unescape(_[1]))
            }
        }
        return d
    }

    function __sc(n,v,d) {
        var date = new Date();
        date.setTime(date.getTime() + (d * 86400000));
        document.cookie = n+"="+v+"; expires="+date.toUTCString()+"; path=/";
    }

    })();
