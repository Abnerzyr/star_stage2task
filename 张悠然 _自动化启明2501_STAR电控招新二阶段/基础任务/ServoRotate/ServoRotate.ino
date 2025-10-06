#include<Servo.h>

//实例化
Servo myservo;


void setup() {
  myservo.attach(9);//连接在9号引脚（用了mega2560的板子）
  Serial.begin(9600);
  
}

void loop() {
   rotate(0,30);
   rotate(30,45);
   rotate(45,90);
   rotate(90,135);
   rotate(135,0);
   //依次转到30,45,90,135并转回0°，循环执行
  

}

void rotate(int begin,int end){
  if(begin<end){ 
    for(int pos=begin;pos<=end;pos++){
      myservo.write(pos);
      delay(20);
      
      }
  }else if(begin>end){
    for(int pos=begin;pos>=end;pos--){
      myservo.write(pos);
      delay(20);
    }
  }else{
      return;
  }//自动判断旋转方向，for循环实现缓慢转动
    delay(2000);//每次旋转后进行延时
}
    
  
 
 