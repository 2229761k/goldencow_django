


// TOP CONTROLS
$('.plus').click(function (e) {
    e.preventDefault();
    var sp_bithumb = parseFloat($(this).prev('#roomcount1').text());
    var sp_upbit = parseFloat($(this).prev('#roomcount2').text());
    var sp_binance = parseFloat($(this).prev('#roomcount3').text());

    if(sp_bithumb<100){
        $(this).prev('#roomcount1').text(sp_bithumb + 1);
    }
    else{
        $(this).next('#roomcount1').text(100);
    }
    if(sp_upbit<100){
        $(this).prev('#roomcount2').text(sp_upbit + 1);
    }
    else{
        $(this).next('#roomcount2').text(100);
    }
    if(sp_binance<100){
        $(this).prev('#roomcount3').text(sp_binance + 1);
    }
    else{
        $(this).next('#roomcount3').text(100);
    }
});

$('.minus').click(function (e) {
    e.preventDefault();
    var sp_bithumb = parseFloat($(this).next('#roomcount1').text());
    var sp_upbit = parseFloat($(this).next('#roomcount2').text());
    var sp_binance = parseFloat($(this).next('#roomcount3').text());

    if(!isNaN(sp_bithumb) && sp_bithumb>0){
        $(this).next('#roomcount1').text(sp_bithumb - 1);
    }
    else {
        $(this).next('#roomcount1').text(0);
    }
    if(!isNaN(sp_upbit) && sp_upbit>0){
        $(this).next('#roomcount2').text(sp_upbit - 1);
    }
    else {
        $(this).next('#roomcount2').text(0);
    }
    if(!isNaN(sp_binance) && sp_binance>0){
        $(this).next('#roomcount3').text(sp_binance - 1);
    }
    else {
        $(this).next('#roomcount3').text(0);
    }
});



var isBithumb=false;
var isUpbit=false;
var isBinance=false;

$('.switch').click(function(e){
    e.preventDefault();
    var bithumb_button = $('#myButton1');
   
    if(isBithumb && bithumb_button)
    {
        isBithumb=false;
        bithumb_button.text('OFF');   
    }else{
        isBithumb=true;
        bithumb_button.text('ON'); 
    }
          
});

$('.switch2').click(function(e){
    e.preventDefault();
    var upbit_button = $('#myButton2');
    if(isUpbit && upbit_button)
    {
        isUpbit=false;
        upbit_button.text('OFF');   
    }else{
        isUpbit=true;
        upbit_button.text('ON'); 
    }
});

$('.switch3').click(function(e){
    e.preventDefault();
    var binance_button = $('#myButton3');
    if(isBinance && binance_button)
    {
        isBinance=false;
        binance_button.text('OFF');   
    }else{
        isBinance=true;
        binance_button.text('ON'); 
    }
});
