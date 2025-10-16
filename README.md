# travel-agency-system

Bu depo, seyahat acentesi için oluşturulan örnek bir yönetim sistemi kod tabanını içerir.

## Admin dashboard şablonu

`travel_agency.admin` modülü, Tailwind CSS kullanılarak tasarlanmış hazır bir yönetim paneli şablonu içerir. Şablon, farklı web framework'lerine kolayca entegre edilebilmesi için statik HTML dosyası olarak saklanır.

```python
from travel_agency.admin import get_dashboard_template

html = get_dashboard_template()
```

Şablon dosyasının tam yolu `travel_agency.admin.TEMPLATE_PATH` değişkeni üzerinden elde edilebilir.
