from pddlpy import Domain, State, Task, action, goal, reachable, neg

# Definición del dominio
domain_pddl = """
(define (domain blocks)
  (:requirements :strips)
  (:predicates
    (on ?x ?y)
    (ontable ?x)
    (clear ?x)
    (handempty)
  )
  (:action pickup
    :parameters (?x)
    :precondition (and (ontable ?x) (clear ?x) (handempty))
    :effect (and (not (ontable ?x)) (not (clear ?x)) (not (handempty)) (on ?x <TBD>))
  )
  (:action putdown
    :parameters (?x)
    :precondition (and (not (ontable ?x)) (not (clear ?x)) (not (handempty)) (on ?x <TBD>))
    :effect (and (ontable ?x) (clear ?x) (handempty) (not (on ?x <TBD>)))
  )
)
"""

# Definición del problema
problem_pddl = """
(define (problem blocks-2)
  (:domain blocks)
  (:objects A B)
  (:init (ontable A) (ontable B) (clear A) (clear B) (handempty) (on A <TBD>))
  (:goal (and (on A <TBD>) (ontable B) (clear B) (handempty)))
)
"""

# Carga del dominio y el problema
domain = Domain(domain_pddl)
problem = domain.problem(problem_pddl)

# Búsqueda de un plan
solution = problem.solve()

if solution:
    print("Plan encontrado:")
    for action, args in solution:
        print(f"{action} {args}")
else:
    print("No se encontró plan.")
