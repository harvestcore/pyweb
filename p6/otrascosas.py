# Bucle for historial

{% for i in range(0,3) %}
{% if session['history'][i] != "" %}
<li>
    <a href="{{ url_for(session.history[i]) }}">{{ session.history[i] }}</a>
</li>
{% endif %}
{% endfor %}



list<pair<letra, numero>> v

iterator a, b


for a = v.begin, a != v.end, ++a
    for b = v.begin, b != v.end, ++b
        if a.second < b.second
            aux = a
            a = b
            b = aux
