from models.challenge import Challenge
from app import db


def create_challenges():
	"""Cria desafios iniciais para o jogo"""

	challenges = [
		# Nível 1: Transformações básicas
		Challenge(
			level=1,
			title="Transformação Mágica",
			description="Aprenda a usar transform para girar, redimensionar e mover elementos.",
			instructions="Faça o quadrado girar 45 graus, aumente seu tamanho em 20% e mova-o 20px para a direita.",
			starter_code="""
.box {
  width: 100px;
  height: 100px;
  background-color: #3498db;
  /* Adicione o seu código abaixo */

}
            """,
			solution_code="""
.box {
  width: 100px;
  height: 100px;
  background-color: #3498db;
  transform: rotate(45deg) scale(1.2) translateX(20px);
}
            """,
			success_criteria="transform: rotate(45deg) scale(1.2) translateX(20px);",
			hint="Combine rotate(), scale() e translateX() em uma única propriedade transform.",
			max_score=100,
			css_property_focus="transform",
			css_effect_category="transform",
			difficulty="easy"
		),

		# Nível 2: Transições
		Challenge(
			level=2,
			title="Transição Suave",
			description="Aprenda a criar transições suaves para propriedades CSS.",
			instructions="Faça o botão mudar de cor gradualmente em 0.5 segundos quando passar o mouse por cima.",
			starter_code="""
.button {
  padding: 10px 20px;
  background-color: #3498db;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  /* Adicione o seu código abaixo */

}

.button:hover {
  background-color: #2980b9;
}
            """,
			solution_code="""
.button {
  padding: 10px 20px;
  background-color: #3498db;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.5s ease;
}

.button:hover {
  background-color: #2980b9;
}
            """,
			success_criteria="transition: background-color 0.5s",
			hint="Use a propriedade transition para definir qual propriedade será animada, a duração e a função de timing.",
			max_score=100,
			css_property_focus="transition",
			css_effect_category="transition",
			difficulty="easy"
		),

		# Nível 3: Animação Keyframe
		Challenge(
			level=3,
			title="Animação Pulsante",
			description="Crie uma animação keyframe para fazer um elemento pulsar.",
			instructions="Crie uma animação que faça o círculo pulsar (escala entre 1 e 1.2) continuamente a cada 2 segundos.",
			starter_code="""
/* Defina a animação keyframe abaixo */


.circle {
  width: 100px;
  height: 100px;
  background-color: #e74c3c;
  border-radius: 50%;
  /* Aplique a animação abaixo */

}
            """,
			solution_code="""
@keyframes pulse {
  0% {
    transform: scale(1);
  }
  50% {
    transform: scale(1.2);
  }
  100% {
    transform: scale(1);
  }
}

.circle {
  width: 100px;
  height: 100px;
  background-color: #e74c3c;
  border-radius: 50%;
  animation: pulse 2s infinite ease-in-out;
}
            """,
			success_criteria="@keyframes pulse",
			hint="Defina um keyframe chamado 'pulse' e aplique-o ao círculo com a propriedade animation.",
			max_score=150,
			css_property_focus="animation",
			css_effect_category="animation",
			difficulty="medium"
		),

		# Nível 4: Efeitos avançados
		Challenge(
			level=4,
			title="Cartão 3D",
			description="Crie um efeito de cartão 3D com perspectiva e hover.",
			instructions="Faça o cartão girar no eixo Y quando passar o mouse por cima, usando perspectiva para criar um efeito 3D.",
			starter_code="""
.container {
  /* Adicione o seu código de perspectiva abaixo */

}

.card {
  width: 200px;
  height: 300px;
  background: linear-gradient(45deg, #3498db, #9b59b6);
  border-radius: 10px;
  /* Adicione a transição abaixo */

}

.container:hover .card {
  /* Adicione o efeito de rotação no hover abaixo */

}
            """,
			solution_code="""
.container {
  perspective: 1000px;
}

.card {
  width: 200px;
  height: 300px;
  background: linear-gradient(45deg, #3498db, #9b59b6);
  border-radius: 10px;
  transition: transform 0.8s ease;
}

.container:hover .card {
  transform: rotateY(30deg);
}
            """,
			success_criteria="perspective: 1000px;",
			hint="Use perspective na container e transform: rotateY() no hover do cartão.",
			max_score=200,
			css_property_focus="perspective, transform",
			css_effect_category="3D",
			difficulty="hard"
		),

		# Nível 5: Animações combinadas
		Challenge(
			level=5,
			title="Botão Mágico",
			description="Crie um botão com múltiplos efeitos visuais combinados.",
			instructions="Crie um botão que tenha um efeito de brilho ao passar o mouse, além de uma pequena elevação com sombra.",
			starter_code="""
/* Defina a animação para o efeito de brilho */


.magic-button {
  position: relative;
  padding: 12px 24px;
  background-color: #9b59b6;
  color: white;
  border: none;
  border-radius: 5px;
  overflow: hidden;
  /* Adicione transições abaixo */

}

.magic-button:hover {
  /* Adicione efeito de elevação */

}

.magic-button::before {
  content: '';
  position: absolute;
  top: -50%;
  left: -50%;
  width: 200%;
  height: 200%;
  background: linear-gradient(45deg, transparent, rgba(255, 255, 255, 0.3), transparent);
  /* Adicione transformação e animação ao pseudo-elemento */

}

.magic-button:hover::before {
  /* Ative a animação no hover */

}
            """,
			solution_code="""
@keyframes shine {
  0% {
    transform: translateX(-100%) rotate(45deg);
  }
  100% {
    transform: translateX(100%) rotate(45deg);
  }
}

.magic-button {
  position: relative;
  padding: 12px 24px;
  background-color: #9b59b6;
  color: white;
  border: none;
  border-radius: 5px;
  overflow: hidden;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.magic-button:hover {
  transform: translateY(-3px);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
}

.magic-button::before {
  content: '';
  position: absolute;
  top: -50%;
  left: -50%;
  width: 200%;
  height: 200%;
  background: linear-gradient(45deg, transparent, rgba(255, 255, 255, 0.3), transparent);
  transform: translateX(-100%) rotate(45deg);
}

.magic-button:hover::before {
  animation: shine 1.5s;
}
            """,
			success_criteria="animation: shine",
			hint="Use @keyframes para o efeito de brilho e transform + box-shadow para o efeito de elevação.",
			max_score=250,
			css_property_focus="animation, transform, box-shadow",
			css_effect_category="combined",
			difficulty="hard"
		),
	]

	# Adiciona os desafios ao banco de dados
	for challenge in challenges:
		db.session.add(challenge)

	db.session.commit()
	print("Desafios iniciais criados com sucesso!")