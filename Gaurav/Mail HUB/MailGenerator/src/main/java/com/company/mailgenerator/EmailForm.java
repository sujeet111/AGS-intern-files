/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.company.mailgenerator;

import java.awt.Dimension;
import java.awt.Toolkit;
import java.util.ArrayList;
import javax.swing.JFileChooser;
import javax.swing.JOptionPane;

/**
 *
 * @author patil
 */
public class EmailForm extends javax.swing.JFrame {

    private String path = null;
    
    public EmailForm() {
        initComponents();
        
        Toolkit toolkit = getToolkit();
        Dimension size = toolkit.getScreenSize();
        setLocation(size.width/2-getWidth()/2,size.height/2-getHeight()/2);
        
        panel2.setVisible(false);
        Mail.Connections.add(new ConnectionMail("smtp.gmail.com","465","trial.gaurav3963@gmail.com", "ABCD@1234"));
        refresh();
    }
    
    private void refresh()
    {
        jTextField1.setText("");
        jTextField3.setText("");
        jTextField4.setText("");
        jTextField5.setText("");
        jTextField6.setText("");
        jTextField7.setText("");
        jTextArea1.setText("");
        jLabel13.setText("");
        jComboBox1.removeAllItems();
        panel2.setVisible(false);
        panel4.setVisible(true);
        for(int i=0; i<Mail.Connections.size();i++)
        {
            jComboBox1.addItem(Mail.Connections.get(i).Email);
        }
    }

    @SuppressWarnings("unchecked")
    
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        panel1 = new java.awt.Panel();
        jLabel5 = new javax.swing.JLabel();
        panel2 = new java.awt.Panel();
        panel3 = new java.awt.Panel();
        jLabel6 = new javax.swing.JLabel();
        jLabel7 = new javax.swing.JLabel();
        jLabel8 = new javax.swing.JLabel();
        jLabel9 = new javax.swing.JLabel();
        jLabel10 = new javax.swing.JLabel();
        jTextField4 = new javax.swing.JTextField();
        jTextField5 = new javax.swing.JTextField();
        jTextField6 = new javax.swing.JTextField();
        jTextField7 = new javax.swing.JTextField();
        jButton3 = new javax.swing.JButton();
        jButton5 = new javax.swing.JButton();
        panel4 = new java.awt.Panel();
        jLabel1 = new javax.swing.JLabel();
        jTextField1 = new javax.swing.JTextField();
        jLabel2 = new javax.swing.JLabel();
        jLabel3 = new javax.swing.JLabel();
        jTextField3 = new javax.swing.JTextField();
        jLabel4 = new javax.swing.JLabel();
        jScrollPane1 = new javax.swing.JScrollPane();
        jTextArea1 = new javax.swing.JTextArea();
        panel5 = new java.awt.Panel();
        jLabel11 = new javax.swing.JLabel();
        jButton2 = new javax.swing.JButton();
        jButton1 = new javax.swing.JButton();
        jComboBox1 = new javax.swing.JComboBox<>();
        jLabel12 = new javax.swing.JLabel();
        jButton4 = new javax.swing.JButton();
        jLabel13 = new javax.swing.JLabel();
        jButton6 = new javax.swing.JButton();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
        setTitle("Email Generator");
        setPreferredSize(new java.awt.Dimension(576, 627));
        setSize(new java.awt.Dimension(576, 627));
        getContentPane().setLayout(new org.netbeans.lib.awtextra.AbsoluteLayout());

        panel1.setLayout(new org.netbeans.lib.awtextra.AbsoluteLayout());

        jLabel5.setFont(new java.awt.Font("Cambria", 0, 48)); // NOI18N
        jLabel5.setText("EMAIL GENERATOR");
        panel1.add(jLabel5, new org.netbeans.lib.awtextra.AbsoluteConstraints(80, 30, -1, -1));

        getContentPane().add(panel1, new org.netbeans.lib.awtextra.AbsoluteConstraints(0, 0, 580, 120));

        panel2.setVisible(false);
        panel2.setLayout(new org.netbeans.lib.awtextra.AbsoluteLayout());

        panel3.setBackground(new java.awt.Color(204, 204, 204));
        panel3.setLayout(new org.netbeans.lib.awtextra.AbsoluteLayout());

        jLabel6.setFont(new java.awt.Font("Cambria", 0, 24)); // NOI18N
        jLabel6.setText("SET PORT AND ACCOUNT");
        panel3.add(jLabel6, new org.netbeans.lib.awtextra.AbsoluteConstraints(50, 20, -1, -1));

        panel2.add(panel3, new org.netbeans.lib.awtextra.AbsoluteConstraints(5, 5, 370, 70));

        jLabel7.setFont(new java.awt.Font("Cambria", 0, 18)); // NOI18N
        jLabel7.setText("Host");
        panel2.add(jLabel7, new org.netbeans.lib.awtextra.AbsoluteConstraints(40, 100, 70, -1));

        jLabel8.setFont(new java.awt.Font("Cambria", 0, 18)); // NOI18N
        jLabel8.setText("Port");
        panel2.add(jLabel8, new org.netbeans.lib.awtextra.AbsoluteConstraints(40, 140, 70, -1));

        jLabel9.setFont(new java.awt.Font("Cambria", 0, 18)); // NOI18N
        jLabel9.setText("Email");
        panel2.add(jLabel9, new org.netbeans.lib.awtextra.AbsoluteConstraints(40, 180, 90, -1));

        jLabel10.setFont(new java.awt.Font("Cambria", 0, 18)); // NOI18N
        jLabel10.setText("Password");
        panel2.add(jLabel10, new org.netbeans.lib.awtextra.AbsoluteConstraints(40, 220, 90, -1));

        jTextField4.setFont(new java.awt.Font("Cambria", 0, 18)); // NOI18N
        jTextField4.setBorder(javax.swing.BorderFactory.createLineBorder(new java.awt.Color(0, 0, 0)));
        panel2.add(jTextField4, new org.netbeans.lib.awtextra.AbsoluteConstraints(140, 100, 200, -1));

        jTextField5.setFont(new java.awt.Font("Cambria", 0, 18)); // NOI18N
        jTextField5.setBorder(javax.swing.BorderFactory.createLineBorder(new java.awt.Color(0, 0, 0)));
        panel2.add(jTextField5, new org.netbeans.lib.awtextra.AbsoluteConstraints(140, 140, 200, -1));

        jTextField6.setFont(new java.awt.Font("Cambria", 0, 18)); // NOI18N
        jTextField6.setBorder(javax.swing.BorderFactory.createLineBorder(new java.awt.Color(0, 0, 0)));
        panel2.add(jTextField6, new org.netbeans.lib.awtextra.AbsoluteConstraints(140, 180, 200, -1));

        jTextField7.setFont(new java.awt.Font("Cambria", 0, 18)); // NOI18N
        jTextField7.setBorder(javax.swing.BorderFactory.createLineBorder(new java.awt.Color(0, 0, 0)));
        panel2.add(jTextField7, new org.netbeans.lib.awtextra.AbsoluteConstraints(140, 220, 200, -1));

        jButton3.setFont(new java.awt.Font("Cambria", 0, 18)); // NOI18N
        jButton3.setText("ADD CONNECTION");
        jButton3.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButton3ActionPerformed(evt);
            }
        });
        panel2.add(jButton3, new org.netbeans.lib.awtextra.AbsoluteConstraints(160, 270, -1, -1));

        jButton5.setFont(new java.awt.Font("Cambria", 0, 18)); // NOI18N
        jButton5.setText("Back");
        jButton5.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButton5ActionPerformed(evt);
            }
        });
        panel2.add(jButton5, new org.netbeans.lib.awtextra.AbsoluteConstraints(40, 270, -1, -1));

        getContentPane().add(panel2, new org.netbeans.lib.awtextra.AbsoluteConstraints(110, 160, 380, 310));

        panel4.setLayout(new org.netbeans.lib.awtextra.AbsoluteLayout());

        jLabel1.setFont(new java.awt.Font("Cambria", 0, 18)); // NOI18N
        jLabel1.setText("Receipients EmailID");
        panel4.add(jLabel1, new org.netbeans.lib.awtextra.AbsoluteConstraints(40, 130, -1, -1));

        jTextField1.setFont(new java.awt.Font("Cambria", 0, 18)); // NOI18N
        jTextField1.setBorder(javax.swing.BorderFactory.createLineBorder(new java.awt.Color(0, 0, 0)));
        panel4.add(jTextField1, new org.netbeans.lib.awtextra.AbsoluteConstraints(210, 130, 250, -1));

        jLabel2.setFont(new java.awt.Font("Cambria", 0, 18)); // NOI18N
        jLabel2.setText("Choose Connection");
        panel4.add(jLabel2, new org.netbeans.lib.awtextra.AbsoluteConstraints(40, 90, -1, -1));

        jLabel3.setFont(new java.awt.Font("Cambria", 0, 18)); // NOI18N
        jLabel3.setText("Subject");
        panel4.add(jLabel3, new org.netbeans.lib.awtextra.AbsoluteConstraints(40, 170, -1, -1));

        jTextField3.setFont(new java.awt.Font("Cambria", 0, 18)); // NOI18N
        jTextField3.setBorder(javax.swing.BorderFactory.createLineBorder(new java.awt.Color(0, 0, 0)));
        panel4.add(jTextField3, new org.netbeans.lib.awtextra.AbsoluteConstraints(210, 170, 250, -1));

        jLabel4.setFont(new java.awt.Font("Cambria", 0, 18)); // NOI18N
        jLabel4.setText("Message");
        panel4.add(jLabel4, new org.netbeans.lib.awtextra.AbsoluteConstraints(40, 210, 110, -1));

        jTextArea1.setColumns(20);
        jTextArea1.setFont(new java.awt.Font("Cambria", 0, 18)); // NOI18N
        jTextArea1.setRows(5);
        jTextArea1.setBorder(javax.swing.BorderFactory.createLineBorder(new java.awt.Color(0, 0, 0)));
        jScrollPane1.setViewportView(jTextArea1);

        panel4.add(jScrollPane1, new org.netbeans.lib.awtextra.AbsoluteConstraints(210, 210, 250, 100));

        panel5.setBackground(new java.awt.Color(204, 204, 204));
        panel5.setLayout(new org.netbeans.lib.awtextra.AbsoluteLayout());

        jLabel11.setFont(new java.awt.Font("Cambria", 0, 36)); // NOI18N
        jLabel11.setText("Write Email");
        panel5.add(jLabel11, new org.netbeans.lib.awtextra.AbsoluteConstraints(120, 20, 230, -1));

        panel4.add(panel5, new org.netbeans.lib.awtextra.AbsoluteConstraints(0, 0, 490, 80));

        jButton2.setFont(new java.awt.Font("Cambria", 0, 18)); // NOI18N
        jButton2.setText("Attach");
        jButton2.setBorder(javax.swing.BorderFactory.createLineBorder(new java.awt.Color(0, 0, 0)));
        jButton2.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButton2ActionPerformed(evt);
            }
        });
        panel4.add(jButton2, new org.netbeans.lib.awtextra.AbsoluteConstraints(200, 320, 100, -1));

        jButton1.setFont(new java.awt.Font("Cambria", 0, 18)); // NOI18N
        jButton1.setText("SEND");
        jButton1.setBorder(javax.swing.BorderFactory.createLineBorder(new java.awt.Color(0, 0, 0)));
        jButton1.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButton1ActionPerformed(evt);
            }
        });
        panel4.add(jButton1, new org.netbeans.lib.awtextra.AbsoluteConstraints(40, 370, 110, 30));

        jComboBox1.setFont(new java.awt.Font("Cambria", 0, 18)); // NOI18N
        jComboBox1.setBorder(javax.swing.BorderFactory.createLineBorder(new java.awt.Color(0, 0, 0)));
        panel4.add(jComboBox1, new org.netbeans.lib.awtextra.AbsoluteConstraints(210, 90, 250, -1));

        jLabel12.setFont(new java.awt.Font("Cambria", 0, 18)); // NOI18N
        jLabel12.setText("Attach File");
        panel4.add(jLabel12, new org.netbeans.lib.awtextra.AbsoluteConstraints(40, 320, -1, -1));

        jButton4.setFont(new java.awt.Font("Cambria", 0, 18)); // NOI18N
        jButton4.setText("Add Connection");
        jButton4.setBorder(javax.swing.BorderFactory.createLineBorder(new java.awt.Color(0, 0, 0)));
        jButton4.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButton4ActionPerformed(evt);
            }
        });
        panel4.add(jButton4, new org.netbeans.lib.awtextra.AbsoluteConstraints(300, 370, 160, 30));
        panel4.add(jLabel13, new org.netbeans.lib.awtextra.AbsoluteConstraints(320, 320, 140, 20));

        jButton6.setFont(new java.awt.Font("Cambria", 0, 18)); // NOI18N
        jButton6.setText("Refresh");
        jButton6.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButton6ActionPerformed(evt);
            }
        });
        panel4.add(jButton6, new org.netbeans.lib.awtextra.AbsoluteConstraints(180, 370, -1, -1));

        getContentPane().add(panel4, new org.netbeans.lib.awtextra.AbsoluteConstraints(40, 130, 490, 420));

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void jButton1ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jButton1ActionPerformed
        String to = jTextField1.getText();
        int Connection = (int)jComboBox1.getSelectedIndex();
        String from = Mail.Connections.get(Connection).Email;
        String subject = jTextField3.getText();
        String message = jTextArea1.getText();
        int a = Mail.sendEmail(message, subject, to, from,path,Connection);
        if(a==1)
        {
            JOptionPane.showMessageDialog(null,"Successfully Sent");
        }
        else
        {
            JOptionPane.showMessageDialog(null,"Problem Occured");
        }
    }//GEN-LAST:event_jButton1ActionPerformed

    private void jButton3ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jButton3ActionPerformed
        
    }//GEN-LAST:event_jButton3ActionPerformed

    private void jButton2ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jButton2ActionPerformed
        JFileChooser chooser = new JFileChooser();
        chooser.showOpenDialog(this);
        path = (chooser.getSelectedFile()).getAbsolutePath();
        jLabel13.setText(path);
    }//GEN-LAST:event_jButton2ActionPerformed

    private void jButton4ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jButton4ActionPerformed
        panel4.setVisible(false);
        panel2.setVisible(true);
    }//GEN-LAST:event_jButton4ActionPerformed

    private void jButton5ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jButton5ActionPerformed
        refresh();
    }//GEN-LAST:event_jButton5ActionPerformed

    private void jButton6ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jButton6ActionPerformed
        refresh();
    }//GEN-LAST:event_jButton6ActionPerformed

    public static void main(String args[]) {
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new EmailForm().setVisible(true);
            }
        });
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JButton jButton1;
    private javax.swing.JButton jButton2;
    private javax.swing.JButton jButton3;
    private javax.swing.JButton jButton4;
    private javax.swing.JButton jButton5;
    private javax.swing.JButton jButton6;
    private javax.swing.JComboBox<String> jComboBox1;
    private javax.swing.JLabel jLabel1;
    private javax.swing.JLabel jLabel10;
    private javax.swing.JLabel jLabel11;
    private javax.swing.JLabel jLabel12;
    private javax.swing.JLabel jLabel13;
    private javax.swing.JLabel jLabel2;
    private javax.swing.JLabel jLabel3;
    private javax.swing.JLabel jLabel4;
    private javax.swing.JLabel jLabel5;
    private javax.swing.JLabel jLabel6;
    private javax.swing.JLabel jLabel7;
    private javax.swing.JLabel jLabel8;
    private javax.swing.JLabel jLabel9;
    private javax.swing.JScrollPane jScrollPane1;
    private javax.swing.JTextArea jTextArea1;
    private javax.swing.JTextField jTextField1;
    private javax.swing.JTextField jTextField3;
    private javax.swing.JTextField jTextField4;
    private javax.swing.JTextField jTextField5;
    private javax.swing.JTextField jTextField6;
    private javax.swing.JTextField jTextField7;
    private java.awt.Panel panel1;
    private java.awt.Panel panel2;
    private java.awt.Panel panel3;
    private java.awt.Panel panel4;
    private java.awt.Panel panel5;
    // End of variables declaration//GEN-END:variables
}
