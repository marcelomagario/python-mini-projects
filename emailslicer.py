"""create a function to receive a e-mail and return the user name and domain


"""

email = input('Digite o e-mail: ')


def emailSlicer(email_entrada):
    email_entrada.strip()
    username = email_entrada[:email_entrada.index("@")]
    domain = email_entrada[email_entrada.index("@") + 1:]
    return username, domain

# implementação
if __name__ == '__main__':

    username, domain = emailSlicer(email)   # marcelo@gmail.com
    print(f'Nome do usuário: {username}')   # marcelo
    print(f'Domínio: {domain}')             # gprint(f'{username}')mail.com

