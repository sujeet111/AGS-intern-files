/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.company.mailgenerator;
import java.io.File;
import java.util.ArrayList;
import java.util.Properties;

import javax.mail.Authenticator;
import javax.mail.Message;
import javax.mail.PasswordAuthentication;
import javax.mail.Session;
import javax.mail.Transport;
import javax.mail.internet.InternetAddress;
import javax.mail.internet.MimeBodyPart;
import javax.mail.internet.MimeMessage;
import javax.mail.internet.MimeMultipart;

/**
 *
 * @author patil
 */
public class Mail {
    
    public static ArrayList<ConnectionMail> Connections = new ArrayList<>();
    
    public static int sendEmail(String message, String subject, String to, String from,String path,int Connection) 
    {
		
	try 
        {
            Properties properties = System.getProperties();
            System.out.println("PROPERTIES "+properties);
            
            String host = Connections.get(Connection).Host;
            System.out.print(host);
            String port = Connections.get(Connection).Port;
            String Email = Connections.get(Connection).Email;
            String Password = Connections.get(Connection).Password;
            
            
            properties.put("mail.smtp.host",host);
            properties.put("mail.smtp.port",port);
            properties.put("mail.smtp.ssl.enable","true");
            properties.put("mail.smtp.auth","true");
		
            Session session=Session.getInstance(properties, new Authenticator() 
            {
                @Override
                protected PasswordAuthentication getPasswordAuthentication() 
                {				
                    return new PasswordAuthentication(Email, Password);
                }
            });
		
            session.setDebug(true);
            MimeMessage m = new MimeMessage(session);	
            m.setFrom(from);
            m.addRecipient(Message.RecipientType.TO, new InternetAddress(to));
            m.setSubject(subject);
            MimeMultipart mimeMultipart = new MimeMultipart();
            MimeBodyPart textMime = new MimeBodyPart();
            MimeBodyPart fileMime = new MimeBodyPart();
		
            try 
            {
		textMime.setText(message);
                
		File file=new File(path);
		fileMime.attachFile(file);
			
		mimeMultipart.addBodyPart(textMime);
		mimeMultipart.addBodyPart(fileMime);
			
            } 
            catch (Exception e) 
            {		
		e.printStackTrace();
            }
		
            m.setContent(mimeMultipart);
            Transport.send(m);
            System.out.println("Sent success...................");
            return 1;
        }
        catch (Exception e) 
        {
            e.printStackTrace();
            return 0;
	}
    }
}
