#ifndef _COM_H_
#define _COM_H_
 
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <errno.h>
#include <unistd.h>
#include <termios.h>
#include <fcntl.h>

#define BUFFER_SIZE 600      /*maximum buffer area*/
 
int set_com_config(int fd,int baud_rate,int data_bits, char parity, int stop_bits);
int open_port( char *dev);
void delayms(int data);
int read_Buffer(int Sfd, char *Sread_buffer);


 
/****************************************/
/************open serial port function****************/ 
/****************************************/
int open_port(char *dev) 
{
  int fd;
  
  printf("open dev [%s]\n",dev);
  //O_NDELAY same O_NONBLOCK。
  fd = open(dev, O_RDWR|O_NOCTTY); 
  if (fd < 0) { 
    perror("open serial port"); 
    return(-1); 
  }
  
  //Restore the serial port to a blocked state 
  //Non-blocking：fcntl(fd,F_SETFL,FNDELAY)
  //Block：fcntl(fd,F_SETFL,0)
  if (fcntl(fd, F_SETFL, 0) < 0)
  {
    perror("fcntl F_SETFL\n");
  }
  /*Test whether it is a terminal device*/ 
  if (isatty(STDIN_FILENO) == 0) {
    perror("standard input is not a terminal device");
  }
  return fd; 
}

/***********************************/
/************Serial port configuration***************/
/***********************************/
int set_com_config(int fd,int baud_rate,int data_bits, char parity, int stop_bits)
{
  struct termios opt;
  int speed;
  if(tcgetattr(fd, &opt) != 0){
    perror("tcgetattr"); 
    return -1;
  }

  /* Set character size*/
  //opt = opt;
  //cfmakeraw(&opt);//Configure to raw mode
  //opt.c_cflag &= ~CSIZE;//c_cflag Control mode flag

  /*Set the baud rate*/ 
  switch (baud_rate) 
  {
    case 2400:  speed = B2400;   break;
    case 4800:  speed = B4800;   break;
    case 9600:  speed = B9600;   break;
    case 19200: speed = B19200;  break;
    case 38400: speed = B38400;  break;
    default:    speed = B115200; break;
  }
  cfsetispeed(&opt, speed); 
  cfsetospeed(&opt, speed); 
  tcsetattr(fd,TCSANOW,&opt);

  opt.c_cflag &= ~CSIZE;

  /*Set data bit*/ 
  switch (data_bits)
  {
    case 7: {opt.c_cflag |= CS7;}break;//7Data bits
    default:{opt.c_cflag |= CS8;}break;//8Data bits 
  }

  /*Set parity bit*/ 
  switch (parity) //N
  {
    case 'n':case 'N': 
    {
      opt.c_cflag &= ~PARENB;//Check bit enable
      opt.c_iflag &= ~INPCK; //Parity check enable
    }break;
    case 'o':case 'O': 
    {
      opt.c_cflag |= (PARODD | PARENB);//PARODD Use odd parity instead of even parity 
      opt.c_iflag |= INPCK;
    }break; 
    case 'e':case 'E': 
    { 
      opt.c_cflag |= PARENB;   
      opt.c_cflag &= ~PARODD;  
      opt.c_iflag |= INPCK;    
    }break;
    case 's':case 'S': /*as no parity*/  
    { 
      opt.c_cflag &= ~PARENB; 
      opt.c_cflag &= ~CSTOPB; 
    }break;
    default:
    {
      opt.c_cflag &= ~PARENB;//Check bit enable     
      opt.c_iflag &= ~INPCK; //Parity check enable          	
    }break; 
  }

  /*Set stop bit*/ 
  switch (stop_bits)
  {
    case 1: {opt.c_cflag &=  ~CSTOPB;} break;
    case 2: {opt.c_cflag |= CSTOPB;}   break;
    default:{opt.c_cflag &=  ~CSTOPB;} break;
  }

  /*Handling unreceived characters*/ 
  tcflush(fd, TCIFLUSH); 

  /*Set the waiting time and minimum received characters*/ 
  opt.c_cc[VTIME]  = 11; 
  opt.c_cc[VMIN] = 0; 

  /*Turn off serial port echo*/
  opt.c_lflag &= ~(ICANON|ECHO|ECHOE|ECHOK|ECHONL|NOFLSH); 
 
  /*Activate new configuration*/ 
  if((tcsetattr(fd, TCSANOW, &opt)) != 0){ 
    perror("tcsetattr"); 
    return -1; 
  }
  return 0; 
}

void delayms(int data)
{
  usleep(data*1000);
}


int read_Buffer(int Sfd, char *Sread_buffer)
{
  int ret = 0;
  int Sleng = 0;
  int times = 0;
  char rbuffer[32]={0};
  do{
    memset(rbuffer, 0, 32);
    Sleng = read(Sfd, rbuffer, 32);
    for(int j=0; j<Sleng; j++){
      if( times*32 + j >= BUFFER_SIZE)
        return -1;
      Sread_buffer[ times*32 + j] = rbuffer[j];
    }
    //printf("%s\n", rbuffer);
    ret = ret + Sleng;
    times++;
    delayms(20);
  }while(Sleng == 32);
  return ret;
}

#endif
