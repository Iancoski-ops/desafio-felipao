nome_heroi = 'Gabriel'
xp_heroi = 3248
nivel_heroi = ''

if xp_heroi <= 1000:
    nivel_heroi = 'Ferro'
elif xp_heroi > 1000 and xp_heroi <= 2000:
    nivel_heroi = 'Bronze'
elif xp_heroi > 2000 and xp_heroi <= 5000:
    nivel_heroi = 'Prata'
elif xp_heroi > 5000 and xp_heroi <= 7000:
    nivel_heroi = 'Ouro'
elif xp_heroi > 7000 and xp_heroi <= 8000:
    nivel_heroi = 'Platina'
elif xp_heroi > 8000 and xp_heroi <= 9000:
    nivel_heroi = 'Ascendente'
elif xp_heroi > 9000 and xp_heroi <= 10000:
    nivel_heroi = 'Imortal'
elif xp_heroi > 10000:
    nivel_heroi = 'Radiante'

print(f'O Herói de nome {nome_heroi} está no nível {nivel_heroi}')