var dateFormat = require('dateformat');
var _relativeDate = require('relative-date');

var filled_star = '<span class="fa fa-star checked"></span>';
var empty_star = '<span class="fa fa-star"></span>';

module.exports = {
    ifeq: function(a, b, options){
      if (a === b) {
        return options.fn(this);
        }
      return options.inverse(this);
    },
    bar: function(){
      return "BAR!";
    },
    formatDate: function(date) {
      return dateFormat(date, "ddd, mmm dS, yyyy, h:MM:ss TT");
    },
    relativeDate: function(date) {
      return _relativeDate(date);
    },
    getStarHTML: function(numOutOfFive) {
      var num = parseInt(numOutOfFive);
      var str='';
      for(var i=0;i<5;i++) {
        if(num > 0) {
          str += filled_star;
        }else {
          str += empty_star;
        }
        num -= 1;
      }
      return str;
    },
    urlencode: function(text) {
      return encodeURIComponent(text.replace("'", ''));
    }
  }