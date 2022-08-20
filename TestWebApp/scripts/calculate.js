//var lhs = '';
//var rhs = '';
expr = ''
var result = 0;
var numberOfKeys = document.querySelectorAll("button").length

for (var iKey = 0; iKey < numberOfKeys; iKey++)
{
    document.querySelectorAll("button")[iKey].addEventListener("click", function () {
        var keyInnerHtml = this.innerHTML;      
        

        switch (keyInnerHtml)
        {
            //case '1':
            //    lhs = lhs + '1';
            //    document.querySelector(".display").innerHTML = lhs;
            //    break;
            //case '2':
            //    lhs = lhs + '2';
            //    document.querySelector(".display").innerHTML = lhs;
            //    break;
            //case '3':
            //    lhs = lhs + '3';
            //    document.querySelector(".display").innerHTML = lhs;
            //    break;
            //case '4':
            //    lhs = lhs + '4';
            //    document.querySelector(".display").innerHTML = lhs;
            //    break;
            //case '5':
            //    lhs = lhs + '5';
            //    document.querySelector(".display").innerHTML = lhs;
            //    break;
            //case '6':
            //    lhs = lhs + '6';
            //    document.querySelector(".display").innerHTML = lhs;
            //    break;
            //case '7':
            //    lhs = lhs + '7';
            //    document.querySelector(".display").innerHTML = lhs;
            //    break;
            //case '8':
            //    lhs = lhs + '8';
            //    document.querySelector(".display").innerHTML = lhs;
            //    break;
            //case '9':
            //    lhs = lhs + '9';
            //    document.querySelector(".display").innerHTML = lhs;
            //    break;
            //case '0':
            //    lhs = lhs + '0';
            //    document.querySelector(".display").innerHTML = lhs;
            //    break;
            //case '+':
            //    val = lhs;
            //    document.querySelector(".display").innerHTML = val + '+' + rhs;
            //    if (rhs == '')
            //        rhs = '0';
            //    rhs = Number(rhs) + Number(val);
            //    lhs = '';
            //    break;
            //case '=':
            //    document.querySelector(".display").innerHTML = rhs.toString();
            //    break;
            //case 'CE':
            //    document.querySelector(".display").innerHTML = '0';
            //    rhs = '0';
            //    break;
            case '1':
                expr += '1';
                document.querySelector(".display").innerHTML = expr;
                break;
            case '2':
                expr += '2';
                document.querySelector(".display").innerHTML = expr;
                break;
            case '3':
                expr += '3';
                document.querySelector(".display").innerHTML = expr;
                break;
            case '4':
                expr += '4';
                document.querySelector(".display").innerHTML = expr;
                break;
            case '5':
                expr += '5';
                document.querySelector(".display").innerHTML = expr;
                break;
            case '6':
                expr += '6';
                document.querySelector(".display").innerHTML = expr;
                break;
            case '7':
                expr += '7';
                document.querySelector(".display").innerHTML = expr;
                break;
            case '8':
                expr += '8';
                document.querySelector(".display").innerHTML = expr;
                break;
            case '9':
                expr += '9';
                document.querySelector(".display").innerHTML = expr;
                break;
            case '0':
                expr += '0';
                document.querySelector(".display").innerHTML = expr;
                break;
            case '+':
                expr += '+'
                document.querySelector(".display").innerHTML = expr;
                break;
            case 'x':
                expr += 'x'
                document.querySelector(".display").innerHTML = expr;
                break;
            case '/':
                expr += '/'
                document.querySelector(".display").innerHTML = expr;
                break;            
            case 'CE':
                document.querySelector(".display").innerHTML = '0';
                expr = '';
                break;
            case '=':
                expr += '='
                
                document.querySelector(".display").innerHTML = expr;
                //Code to evaluate the expression - TODO
                var temp = '';
                for (var i = 0; i < expr.length; i++) {
                    console.log(expr.charAt(i));                    
                    if ((Number(expr.charAt(i))) >= 0 && (Number(expr.charAt(i)) <= 9))
                    {
                        temp = temp + expr.charAt(i);
                    }
                    if (expr.charAt(i) == '+') {
                        result = result + Number(temp);
                        temp = '';
                    }
                }
                document.querySelector(".display").innerHTML = result.toString();
                
        }
    })
}