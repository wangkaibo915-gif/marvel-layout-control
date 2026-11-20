# Iron Man — контрольная группа

Выбран слайд Iron Man из макета `Marvel-Themed Merchandise Landing Page (Community).pix`. Целевой размер одного экрана: **1440 × 1024 px**. Экспортированный эталон находится в `assets/reference.png`; страница `reference.html` показывает этот эталон.

## Запуск

В каталоге проекта выполните `npm ci`, затем в первом терминале `npm run serve`. Во втором терминале запустите `npm run backstop:test`. Конфигурация `backstop.json` сравнивает страницу с эталоном при размере 1440 × 1024. Команду `npm run backstop:reference` следует использовать только после изменения исходного эталона.

## Сценарий Galen

Файл `galen/ironman.spec` проверяет основные области страницы. После установки Galen Framework и ChromeDriver:

```sh
galen check galen/ironman.spec --url http://127.0.0.1:8080/ --size 1440x1024
```

**Статус:** сценарии подготовлены, но фактические успешные запуски BackstopJS и Galen для этой группы пока не зафиксированы.
