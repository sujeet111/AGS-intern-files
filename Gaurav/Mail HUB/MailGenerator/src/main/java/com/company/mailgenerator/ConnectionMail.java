/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.company.mailgenerator;

/**
 *
 * @author patil
 */
public class ConnectionMail {
    
    public String Host;
    public String Port;
    public String Email;
    public String Password;
    
    public ConnectionMail(String Host,String Port,String Email,String Password)
    {
        this.Host = Host;
        this.Port = Port;
        this.Email = Email;
        this.Password = Password;
    }
}
