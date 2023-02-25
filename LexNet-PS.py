while 1==1:
    import nmap
    import colorama
    from colorama import Fore, Back, Style
    colorama.init(autoreset=True)

    scanner = nmap.PortScanner()  



    print("""                                                                                         
                                                                                                    
                                                                                                    
                                                                                                    
                            .~?JJJYYYYYYYYYYYY555555YYYYYYYYYYYYYYYJ!:                              
                         :!YPBBBGGGGBBBBBBBBBBB#####BBBBBBBBBBBBBGGBBB5?~.                          
                     .~J5GB##B#BGGGGGBBBBBBBBBBBBBBBBBBBBBBBBGGGGGB#####BGY7:                       
                   ^?P###BBBBBBBBGBB#&#BBBBBBBBBBBBBBBBBBBGGGGPGGGBBB#BBB###B5!.                    
                :!YBBBBBBBBBB####BB##BBBBBBBBBBBBBBBBBBGPPPPPGPPPPGGGGBBBBB####GJ~.                 
              .JPBBBGGBB##########B##BBBBBBBBBBBBBBGPPPPPPPPPPPPPGGGPPPGGGBB#####BP!                
              .~YPPPGGBBBBBBB##########BBBBBBBBBB##BBBBBGBBBBBBB#BBBBBBBBBBBBGGGG5?:                
                 :7Y5555PGGGGGGGGGGGGGGGGGGGGGGGBBBBBBGBBGGGGGGGGGGGGGGGGPP55P5J~.                  
                   .~J5555PGGPPGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGPPGGPPPGPP555Y7:                     
                      :7Y555PGPPPPPPGGGGGGGGGGGGGGGGGGGGGGGGGGPPPPPPGPP555J~.                       
                        .~?YY5PPPPPPPPGGGGGGGGGGGGGGGGGGGGGGPPPPPPPP555Y7:                          
                           :7JY55PPPPPPGGGGGGGGGGGGGGGGGGGGPPPPPP55YY?~.                            
                             .~?Y55PPPPPGGGGGGBGGGGGBGGGGGPPPPP555J7:                               
                                ^7Y55PPPPGGBBBBGGGGGBGBGGPPPP555?~.                                 
                                  .~J555PPPGGGGGGGGGGGGPPPP55Y7^                                    
                                     ^7Y55PPGGGGGGGGGGGP555J~.                                      
                                       .!Y5PPGGGGGGGGPPP5?^                                         
                                         .^7Y5PGGGGGP5J!:                                           
                                            .~?5GGPY!:                                              
                                               .!?^                                                 
    """)

    print(f"""
    __              _   __     __        ____  _____
   / /   ___  _  __/ | / /__  / /_      / __ \/ ___/
  / /   / _ \| |/_/  |/ / _ \/ __/_____/ /_/ /\__ \ 
 / /___/  __/>  </ /|  /  __/ /_/_____/ ____/___/ / 
/_____/\___/_/|_/_/ |_/\___/\__/     /_/    /____/  
                                                                                                                                                                                                
    """)

    print(f"----------------------------------------------------------------------------")

    ip_addr = input(f"Enter the IP address you want to scan: ")
    print("The IP you entered is:  ", ip_addr)
    type(ip_addr)

    resp = input("""\nPlease enter the type of scan you want to run
                [1] SYN ACK Scan
                [2] UDP Scan
                [3]Comprehensive Scan \n""")
    print("You have selected option: ", resp)

    if resp == '1':
        print("Nmap Version: ", scanner.nmap_version())
        scanner.scan(ip_addr, '1-1024', '-v -sS')
        print(scanner.scaninfo())
        print("IP Status: ", scanner[ip_addr].state())
        print(scanner[ip_addr].all_protocols())
        print("Open ports: ", scanner[ip_addr]['tcp'].keys())

    if resp == '2':
        print("Nmap Version: ", scanner.nmap_version())
        scanner.scan(ip_addr, '1-1024', '-v -sU')
        print(scanner.scaninfo())
        print("IP Status: ", scanner[ip_addr].state())
        print(scanner[ip_addr].all_protocols())
        print("Open ports: ", scanner[ip_addr]['udp'].keys())

    if resp == '3':     
        print("Nmap Version: ", scanner.nmap_version())
        scanner.scan(ip_addr, '1-1024', '-v -sS -sV -sC -A -O')
        print(scanner.scaninfo())
        print("IP Status: ", scanner[ip_addr].state())
        print(scanner[ip_addr].all_protocols())
        print("Open ports: ", scanner[ip_addr]['udp'].keys())
        if resp == '4':
            print("Please enter a valid scan option")
