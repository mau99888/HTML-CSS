import customtkinter as customtkinter
#configurando a aparência
customtkinter.set_appearance_mode('dark')




#Criação da janela principal
app=customtkinter.CTk()
app.title('Sistema de Login')
app.geometry('300x300')

#label
label_usuario=customtkinter.CTkLabel(app,text='Paciente:')
label_usuario.pack(pady=10)

#entry
campo_usuario=customtkinter.CTkEntry(app,placeholder_text='Digite seu Nome...')
campo_usuario.pack(pady=10)

label_usuario=customtkinter.CTkLabel(app,text='Idade:')
label_usuario.pack(pady=10)

#entry
campo_usuario=customtkinter.CTkEntry(app,placeholder_text='Digite sua Idade...')
campo_usuario.pack(pady=10)

label_usuario=customtkinter.CTkLabel(app,text='Telefone:')
label_usuario.pack(pady=10)

#entry
campo_usuario=customtkinter.CTkEntry(app,placeholder_text='(11) 99999-9999 ...')
campo_usuario.pack(pady=10)

label_usuario=customtkinter.CTkLabel(app,text='Usuário:')
label_usuario.pack(pady=10)

#entry
campo_usuario=customtkinter.CTkEntry(app,placeholder_text='Digite seu CPF...')
campo_usuario.pack(pady=10)



#label
label_senha=customtkinter.CTkLabel(app,text='Senha:')
label_senha.pack(pady=10)

#entry
campo_senha=customtkinter.CTkEntry(app,placeholder_text='Digite sua senha...')
campo_senha.pack(pady=10)


#button
botao_login=customtkinter.CTkButton(app,text='Login',command='validar_login')
botao_login.pack(pady=10)
#campo feedback de login
resultado_login=customtkinter.CTkLabel(app,text='Paciente cadastrado com sucesso!')
resultado_login.pack(pady=10)

resultado_login=customtkinter.CTkLabel(app,text='Paciente mais novo: 1 mês!')
resultado_login.pack(pady=10)

resultado_login=customtkinter.CTkLabel(app,text='Paciente mais velho: 98 anos!')
resultado_login.pack(pady=10)

resultado_login=customtkinter.CTkLabel(app,text='Número total de pacientes: 3590!!')
resultado_login.pack(pady=10)








#Iniciar a aplicação
app.mainloop()



