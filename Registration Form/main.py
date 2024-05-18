import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup

class RegistrationApp(App):
    def build(self):
        self.title="Registration Form"
        layout=BoxLayout(orientation="vertical",padding=30,spacing=10)
        
        head=Label(text="Python User Registration App",font_size=26,bold=True,height=40)
        name=Label(text="Name:",font_size=18)
        self.name_input=TextInput(multiline=False,font_size=18)
        email=Label(text="Email:",font_size=18)
        self.email_input=TextInput(multiline=False,font_size=18)
        pwd=Label(text="Password:",font_size=18)
        self.pwd_input=TextInput(multiline=False,font_size=18,password=True)
        cnf_pwd=Label(text="Confirm Password:",font_size=18)
        self.cnfpwd_input=TextInput(multiline=False,font_size=18,password=True)
        
        submit=Button(text="Register",font_size=18,on_press=self.register)
        
        layout.add_widget(head)
        layout.add_widget(name)
        layout.add_widget(self.name_input)
        layout.add_widget(email)
        layout.add_widget(self.email_input)
        layout.add_widget(pwd)
        layout.add_widget(self.pwd_input)
        layout.add_widget(cnf_pwd)
        layout.add_widget(self.cnfpwd_input)
        layout.add_widget(submit)
        return layout
    
    def register(self,instance):
        name=self.name_input.text
        email=self.email_input.text
        pwd=self.pwd_input.text
        cnf_pwd=self.cnfpwd_input.text
        
        if name.strip()=='' or email.strip()=='' or pwd.strip()=='' or cnf_pwd.strip()=='':
            msg="Please fill in all fields"
            
        elif pwd!=cnf_pwd:
            msg="Password Do Not Match"
            
        else:
            filename=name+'.txt'
            with open(filename,'w') as f:
                f.write('Name: {}\n'.format(name))
                f.write('Email: {}\n'.format(email))
                f.write('Password: {}\n'.format(pwd))
            msg="Registration Successful!\nName: {}\nEmail: {}".format(name,email)
                
            
        popup=Popup(title="Registration Status", content=Label(text=msg),size_hint=(None,None),size=(400,200))
        popup.open()
    
if __name__=="__main__":
    RegistrationApp().run()