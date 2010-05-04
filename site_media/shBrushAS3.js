/*
 * AS3 Syntax
 * @author Mark Walters
 * http://www.digitalflipbook.com
 * 
 * JsMin
 * Javascript Compressor
 * http://www.crockford.com/
 * http://www.smallsharptools.com/
*/

dp.sh.Brushes.AS3=function()
{var definitions='class interface package';var keywords='Array Boolean Date decodeURI decodeURIComponent encodeURI encodeURIComponent escape '+'int isFinite isNaN isXMLName Number Object parseFloat parseInt '+'String trace uint unescape XML XMLList '+'Infinity -Infinity NaN undefined '+'as delete instanceof is new typeof '+'break case catch continue default do each else finally for if in '+'label return super switch throw try while with '+'dynamic final internal native override private protected public static '+'...rest const extends function get implements namespace set '+'import include use '+'AS3 flash_proxy object_proxy '+'false null this true '+'void Null';this.regexList=[{regex:dp.sh.RegexLib.SingleLineCComments,css:'comment'},{regex:dp.sh.RegexLib.MultiLineCComments,css:'blockcomment'},{regex:dp.sh.RegexLib.DoubleQuotedString,css:'string'},{regex:dp.sh.RegexLib.SingleQuotedString,css:'string'},{regex:new RegExp('^\\s*#.*','gm'),css:'preprocessor'},{regex:new RegExp(this.GetKeywords(definitions),'gm'),css:'definition'},{regex:new RegExp(this.GetKeywords(keywords),'gm'),css:'keyword'},{regex:new RegExp('var','gm'),css:'variable'}];this.CssClass='dp-as';this.Style='.dp-as .comment { color: #009900; font-style: italic; }'+'.dp-as .blockcomment { color: #3f5fbf; }'+'.dp-as .string { color: #990000; }'+'.dp-as .preprocessor { color: #0033ff; }'+'.dp-as .definition { color: #9900cc; font-weight: bold; }'+'.dp-as .keyword { color: #0033ff; }'+'.dp-as .variable { color: #6699cc; font-weight: bold; }';}
dp.sh.Brushes.AS3.prototype=new dp.sh.Highlighter();dp.sh.Brushes.AS3.Aliases=['as','actionscript','ActionScript','as3','AS3'];