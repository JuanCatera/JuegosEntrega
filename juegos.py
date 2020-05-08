import hangman
import reversegam
import tictactoeModificado
import json    #Utilizo json porque el formato de diccionario me es mas facil para guardar los datos del jugador.
import PySimpleGUI as sg

juegos = ['Ahorcado', 'Ta-Te-Ti','Otello']
datos_jugador= {}

archivo = open ('jugador.txt','w')

layout = [ [sg.Text('Ingrese su nombre:'), sg.Input(key = 'nom')],
		   [sg.Text('Elija el juego a jugar:')],
		   [sg.Text('Opciones:'), sg.Listbox(juegos ,size = (20,5), key= 'lista')],
		   [sg.Button('Ok'), sg.Button('Cancel')]  ]

window = sg.Window('Window', layout)
event, values = window.read()
window.close()
datos_jugador['Nombre'] = values['nom']
datos_jugador['Juego'] = values['lista'][0]
json.dump(datos_jugador,archivo)

def main(args):
		opcion = values['lista'][0]
		if opcion == 'Ahorcado':
			hangman.main()
		elif opcion == 'Ta-Te-Ti':
			tictactoeModificado.main()
		elif opcion == 'Otello':
			reversegam.main()


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
