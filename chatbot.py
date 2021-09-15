from nltk.chat.util import Chat, reflections 
mis_reflexiones = {
"ir": "fui",
"hola":"hey"
}
pares =[
		[
			r"mi nombre es (.*)",
			["Hola %1, como estas?", ]
		],
		[
			r"cual es tu nombre ?",
			["mi nombre es Chatbot ?", ]
		],
		[
			r"como estas?",
			["bien y tu?", ]
		],
		[
			r"disculpa (.*)",
			["no pasa nada",]
		],
		[
			r"hola buenas",
			["hola que tal",]
		],
		[
			r"que (.*) quieres ?",
			["nada gracias",]
		],
		[
			r."(.*) creado ?",
			["fui creado hoy",]
		],
		[
			r"finalizar",
			["adios fue bueno hablar contigo",]
		],
]
def chatear():
		print("Hola") #mensaje por defecto
		chat = Chat(pares, mis_reflexiones)
		chat.converse()
if __name__ == "__main__":
	chatear()
	
chatear()