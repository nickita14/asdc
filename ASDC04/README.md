# Индивидуальная работа №4: Методы доступа к элементам массива

Проект представляет собой реализацию многомерного массива в Python с использованием различных методов доступа к элементам.

## Описание

В этом проекте реализованы три метода доступа к элементам многомерного массива:
1. Прямой доступ
2. Доступ с использованием векторов Айлиффа
3. Доступ с использованием определяющих векторов

## Примеры

```
mda = MultiDimensionalArray((1000, 1000, 1000))
print(mda.direct_access((500, 500, 500)))
print(mda.illiffe_vector_access([500, 500, 500]))
print(mda.defining_vector_access((500, 500, 500)))
```

Этот код создаст многомерный массив размером 1000x1000x1000 и получит доступ к элементу в позиции (500, 500, 500) с использованием каждого из трех методов.