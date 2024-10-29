# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 17:54:50 2024

@author: Alex
"""
   
from flask import Flask, jsonify
import os  
def CrearApiMaquinas():
    maquinapi = Flask(__name__)
    
    # Lista 1.
    @maquinapi.route("/api/ejercicios", methods = ['GET'])
    def obtener_ejercicios():
        datos = {
            "musculos": {
                "abdominales": [
                    {
                        "nombre": "Crunch",
                        "tipo": "Aislamiento",
                        "dificultad": "Baja",
                        "series": 3,
                        "repeticiones": 15
                    },
                    {
                        "nombre": "Plancha",
                        "tipo": "Estabilidad",
                        "dificultad": "Media",
                        "series": 3,
                        "repeticiones": "30 segundos"
                    },
                    {
                        "nombre": "Elevación de piernas",
                        "tipo": "Aislamiento",
                        "dificultad": "Media",
                        "series": 3,
                        "repeticiones": 12
                    },
                    {
                        "nombre": "Bicicleta",
                        "tipo": "Aislamiento",
                        "dificultad": "Media",
                        "series": 3,
                        "repeticiones": 15
                    }
                ],
                "biceps": [
                    {
                        "nombre": "Curl con barra",
                        "tipo": "Aislamiento",
                        "dificultad": "Baja",
                        "series": 4,
                        "repeticiones": 10
                    },
                    {
                        "nombre": "Curl alterno con mancuernas",
                        "tipo": "Aislamiento",
                        "dificultad": "Baja",
                        "series": 4,
                        "repeticiones": 12
                    },
                    {
                        "nombre": "Curl en predicador",
                        "tipo": "Aislamiento",
                        "dificultad": "Media",
                        "series": 3,
                        "repeticiones": 10
                    },
                    {
                        "nombre": "Curl concentrado",
                        "tipo": "Aislamiento",
                        "dificultad": "Media",
                        "series": 3,
                        "repeticiones": 12
                    }
                ],
                "triceps": [
                    {
                        "nombre": "Fondos",
                        "tipo": "Compuesto",
                        "dificultad": "Media",
                        "series": 3,
                        "repeticiones": 8
                    },
                    {
                        "nombre": "Extensión de tríceps con cuerda",
                        "tipo": "Aislamiento",
                        "dificultad": "Baja",
                        "series": 4,
                        "repeticiones": 10
                    },
                    {
                        "nombre": "Press de tríceps en banco",
                        "tipo": "Compuesto",
                        "dificultad": "Media",
                        "series": 3,
                        "repeticiones": 10
                    },
                    {
                        "nombre": "Extensión de tríceps con mancuerna",
                        "tipo": "Aislamiento",
                        "dificultad": "Baja",
                        "series": 3,
                        "repeticiones": 12
                    }
                ],
                "quadriceps": [
                    {
                        "nombre": "Sentadillas",
                        "tipo": "Compuesto",
                        "dificultad": "Media",
                        "series": 4,
                        "repeticiones": 10
                    },
                    {
                        "nombre": "Prensa de piernas",
                        "tipo": "Compuesto",
                        "dificultad": "Media",
                        "series": 4,
                        "repeticiones": 12
                    },
                    {
                        "nombre": "Zancadas",
                        "tipo": "Compuesto",
                        "dificultad": "Media",
                        "series": 3,
                        "repeticiones": 12
                    },
                    {
                        "nombre": "Extensión de piernas",
                        "tipo": "Aislamiento",
                        "dificultad": "Baja",
                        "series": 3,
                        "repeticiones": 15
                    }
                ],
                "pecho": [
                    {
                        "nombre": "Press de banca",
                        "tipo": "Compuesto",
                        "dificultad": "Media",
                        "series": 4,
                        "repeticiones": 10
                    },
                    {
                        "nombre": "Flexiones",
                        "tipo": "Compuesto",
                        "dificultad": "Baja",
                        "series": 3,
                        "repeticiones": 15
                    },
                    {
                        "nombre": "Aperturas con mancuernas",
                        "tipo": "Aislamiento",
                        "dificultad": "Media",
                        "series": 3,
                        "repeticiones": 12
                    },
                    {
                        "nombre": "Press inclinado con mancuernas",
                        "tipo": "Compuesto",
                        "dificultad": "Media",
                        "series": 3,
                        "repeticiones": 10
                    }
                ],
                "espalda": [
                    {
                        "nombre": "Dominadas",
                        "tipo": "Compuesto",
                        "dificultad": "Alta",
                        "series": 3,
                        "repeticiones": 8
                    },
                    {
                        "nombre": "Remo con barra",
                        "tipo": "Compuesto",
                        "dificultad": "Media",
                        "series": 4,
                        "repeticiones": 10
                    },
                    {
                        "nombre": "Jalón al pecho",
                        "tipo": "Compuesto",
                        "dificultad": "Media",
                        "series": 3,
                        "repeticiones": 12
                    },
                    {
                        "nombre": "Remo en máquina",
                        "tipo": "Compuesto",
                        "dificultad": "Baja",
                        "series": 3,
                        "repeticiones": 10
                    }
                ]
                }
            }
        return jsonify(datos)

    
    @maquinapi.route("/api/maquinasGIMNASIO", methods = ['GET'])
    def obtener_ejercicios():
        datos = {
          "gimnasio": {
            "maquinas": [
              {
                "nombre": "Press de banca",
                "tipo": "pesas libres",
                "grupoMuscular": ["Pecho", "Tríceps", "Hombros"]
              },
              {
                "nombre": "Leg Press",
                "tipo": "máquina",
                "grupoMuscular": ["Cuádriceps", "Glúteos", "Isquiotibiales"]
              },
              {
                "nombre": "Remo sentado",
                "tipo": "máquina",
                "grupoMuscular": ["Espalda", "Bíceps"]
              },
              {
                "nombre": "Máquina de abdominales",
                "tipo": "máquina",
                "grupoMuscular": ["Abdominales"]
              },
              {
                "nombre": "Máquina de extensiones de piernas",
                "tipo": "máquina",
                "grupoMuscular": ["Cuádriceps"]
              },
              {
                "nombre": "Máquina de curl de piernas",
                "tipo": "máquina",
                "grupoMuscular": ["Isquiotibiales"]
              },
              {
                "nombre": "Press militar",
                "tipo": "pesas libres",
                "grupoMuscular": ["Hombros", "Tríceps"]
              },
              {
                "nombre": "Pulsómetros",
                "tipo": "cardio",
                "grupoMuscular": ["Cardiovascular"]
              },
              {
                "nombre": "Caminadora",
                "tipo": "cardio",
                "grupoMuscular": ["Cardiovascular", "Piernas"]
              },
              {
                "nombre": "Bicicleta estática",
                "tipo": "cardio",
                "grupoMuscular": ["Cardiovascular", "Piernas"]
              },
              {
                "nombre": "Pectoral Machine",
                "tipo": "máquina",
                "grupoMuscular": ["Pecho", "Hombros"]
              },
              {
                "nombre": "Máquina de dorsales",
                "tipo": "máquina",
                "grupoMuscular": ["Espalda"]
              },
              {
                "nombre": "Abductor Machine",
                "tipo": "máquina",
                "grupoMuscular": ["Glúteos", "Muslos"]
              },
              {
                "nombre": "Adductor Machine",
                "tipo": "máquina",
                "grupoMuscular": ["Muslos internos"]
              },
              {
                "nombre": "Smith Machine",
                "tipo": "máquina",
                "grupoMuscular": ["Varios"]
              },
              {
                "nombre": "Trapecio Machine",
                "tipo": "máquina",
                "grupoMuscular": ["Trapecio", "Espalda"]
              },
              {
                "nombre": "Máquina de fondos",
                "tipo": "máquina",
                "grupoMuscular": ["Tríceps", "Pecho"]
              },
              {
                "nombre": "Máquina de remo inclinado",
                "tipo": "máquina",
                "grupoMuscular": ["Espalda", "Bíceps", "Piernas"]
              },
              {
                "nombre": "Máquina de press de piernas",
                "tipo": "máquina",
                "grupoMuscular": ["Cuádriceps", "Glúteos"]
              }
            ]
          }
        }
        
    if __name__ == '__main__':
        port = int(os.environ.get('PORT', 5000))
        maquinapi.run(host='0.0.0.0', port=port)
        