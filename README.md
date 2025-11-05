

@startuml
title Mealy Machine

state A
state B
state C
state D
state E

A --> A : 0/A
A --> B : 1/B
B --> C : 0/A
B --> D : 1/B
C --> D : 0/C
C --> B : 1/B
D --> B : 0/B
D --> C : 1/C
E --> D : 0/C
E --> E : 1/C

@enduml



@startuml
title Moore Machine

state "A_A\noutput A" as A_A
state "B_B\noutput B" as B_B
state "C_A\noutput A" as C_A
state "C_C\noutput C" as C_C
state "D_B\noutput B" as D_B
state "D_C\noutput C" as D_C
state "E_C\noutput C" as E_C

A_A --> A_A : 0
A_A --> B_B : 1
B_B --> C_A : 0
B_B --> D_B : 1
C_A --> D_C : 0
C_A --> B_B : 1
C_C --> D_C : 0
C_C --> B_B : 1
D_B --> B_B : 0
D_B --> C_C : 1
D_C --> B_B : 0
D_C --> C_C : 1
E_C --> D_C : 0
E_C --> E_C : 1

@enduml
