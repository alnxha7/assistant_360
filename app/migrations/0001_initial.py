# Generated by Django 4.2.3 on 2024-08-27 15:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bank',
            fields=[
                ('bank_id', models.AutoField(primary_key=True, serialize=False)),
                ('holder', models.CharField(max_length=100, verbose_name='holder')),
                ('card', models.CharField(max_length=100, verbose_name='card')),
                ('cvv', models.CharField(max_length=100, verbose_name='cvv')),
                ('exp', models.CharField(max_length=100, verbose_name='exp')),
                ('bal', models.CharField(max_length=100, verbose_name='bal')),
            ],
        ),
        migrations.CreateModel(
            name='bill',
            fields=[
                ('billno', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.CharField(max_length=100, verbose_name='date')),
                ('total', models.CharField(max_length=100, verbose_name='date')),
                ('order_status', models.CharField(max_length=100, verbose_name='order_status')),
            ],
        ),
        migrations.CreateModel(
            name='cart',
            fields=[
                ('cart_id', models.AutoField(primary_key=True, serialize=False)),
                ('pqty', models.CharField(max_length=100, verbose_name='pqty')),
                ('cart_date', models.CharField(max_length=100, verbose_name='date')),
                ('cart_status', models.CharField(max_length=100, verbose_name='cart_status')),
            ],
        ),
        migrations.CreateModel(
            name='district',
            fields=[
                ('district_id', models.AutoField(primary_key=True, serialize=False)),
                ('district', models.CharField(max_length=100, verbose_name='district')),
            ],
        ),
        migrations.CreateModel(
            name='hotel',
            fields=[
                ('hotel_id', models.AutoField(primary_key=True, serialize=False)),
                ('hotel_name', models.CharField(max_length=100, verbose_name='hotel_name')),
                ('hotel_licence', models.CharField(max_length=100, verbose_name='hotel_licence')),
                ('hotel_address', models.CharField(max_length=500, verbose_name='hotel_address')),
                ('category', models.CharField(max_length=100, verbose_name='category')),
                ('hotel_contact', models.CharField(max_length=100, verbose_name='hotel_contact')),
                ('hotel_mail', models.CharField(max_length=100, verbose_name='hotel_mail')),
                ('photo', models.FileField(upload_to='images/', verbose_name='photo:')),
                ('status', models.CharField(max_length=100, verbose_name='status')),
                ('district', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.district')),
            ],
        ),
        migrations.CreateModel(
            name='locations',
            fields=[
                ('location_id', models.AutoField(primary_key=True, serialize=False)),
                ('location', models.CharField(max_length=100, verbose_name='location')),
                ('distict', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.district')),
            ],
        ),
        migrations.CreateModel(
            name='login',
            fields=[
                ('logid', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100, verbose_name='username')),
                ('password', models.CharField(max_length=100, verbose_name='password')),
                ('role', models.CharField(max_length=10, verbose_name='role')),
            ],
        ),
        migrations.CreateModel(
            name='menu',
            fields=[
                ('menu_id', models.AutoField(primary_key=True, serialize=False)),
                ('menu_name', models.CharField(max_length=100, verbose_name='menu_name')),
                ('menu_price', models.CharField(max_length=100, verbose_name='menu_price')),
                ('menu_photo', models.FileField(max_length=1000, upload_to='images/', verbose_name='menu_photo')),
                ('hotel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.hotel')),
            ],
        ),
        migrations.CreateModel(
            name='staff',
            fields=[
                ('staff_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='staffname')),
                ('address', models.CharField(max_length=500, verbose_name='address')),
                ('aadhaar_no', models.CharField(max_length=100, verbose_name='aadhaar')),
                ('phone_no', models.CharField(max_length=100, verbose_name='phone_no')),
                ('email', models.CharField(max_length=100, verbose_name='email')),
                ('category', models.CharField(max_length=100, verbose_name='category')),
                ('exp', models.CharField(max_length=100, verbose_name='experience')),
                ('basic_salary', models.CharField(max_length=100, verbose_name='basic_salary')),
                ('photo', models.FileField(upload_to='images/', verbose_name='photo:')),
                ('status', models.CharField(max_length=100, verbose_name='status:')),
                ('district', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.district')),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.locations')),
                ('login', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.login')),
            ],
        ),
        migrations.CreateModel(
            name='state',
            fields=[
                ('state_id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.CharField(max_length=100, verbose_name='state')),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100, verbose_name='username')),
                ('useraddress', models.CharField(max_length=500, verbose_name='address')),
                ('phoneno', models.CharField(max_length=100, verbose_name='Phone_no')),
                ('useremail', models.CharField(max_length=100, verbose_name='email')),
                ('Photo', models.FileField(upload_to='images/', verbose_name='photo:')),
                ('status', models.CharField(max_length=100, verbose_name='status:')),
                ('district', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.district')),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.locations')),
                ('login', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.login')),
                ('state', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.state')),
            ],
        ),
        migrations.CreateModel(
            name='taxibooking',
            fields=[
                ('booking_id', models.AutoField(primary_key=True, serialize=False)),
                ('pickup_point', models.CharField(max_length=100, verbose_name='pickup_point')),
                ('destination_point', models.CharField(max_length=100, verbose_name='destination_point')),
                ('travel_time', models.CharField(max_length=100, verbose_name='travel_time')),
                ('travel_date', models.CharField(max_length=100, verbose_name='travel_date')),
                ('booking_date', models.CharField(max_length=100, verbose_name='travel_date')),
                ('amount', models.CharField(max_length=100, verbose_name='amount')),
                ('km', models.CharField(max_length=100, verbose_name='km')),
                ('status', models.CharField(max_length=100, verbose_name='status')),
                ('taxiid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.staff')),
                ('userid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.user')),
            ],
        ),
        migrations.AddField(
            model_name='staff',
            name='state',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.state'),
        ),
        migrations.CreateModel(
            name='orderlist',
            fields=[
                ('orderno', models.AutoField(primary_key=True, serialize=False)),
                ('billno', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.bill')),
                ('cart_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.cart')),
            ],
        ),
        migrations.CreateModel(
            name='menutype',
            fields=[
                ('type_id', models.AutoField(primary_key=True, serialize=False)),
                ('type_name', models.CharField(max_length=100, verbose_name='type_name')),
                ('hotel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.hotel')),
            ],
        ),
        migrations.CreateModel(
            name='menustock',
            fields=[
                ('stock_id', models.AutoField(primary_key=True, serialize=False)),
                ('qty', models.CharField(max_length=100, verbose_name='qty')),
                ('date', models.CharField(max_length=100, verbose_name='date')),
                ('hotel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.hotel')),
                ('menu_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.menu')),
            ],
        ),
        migrations.AddField(
            model_name='menu',
            name='menu_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.menutype'),
        ),
        migrations.CreateModel(
            name='labour',
            fields=[
                ('labour_id', models.AutoField(primary_key=True, serialize=False)),
                ('from_date', models.CharField(max_length=100, verbose_name='from date')),
                ('to_date', models.CharField(max_length=100, verbose_name='to date')),
                ('category', models.CharField(max_length=100, verbose_name='category')),
                ('desc', models.CharField(max_length=500, verbose_name='description')),
                ('amount', models.CharField(max_length=100, verbose_name='amount')),
                ('reject', models.CharField(max_length=100, verbose_name='reject')),
                ('status', models.CharField(max_length=100, verbose_name='status')),
                ('staff', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.staff')),
                ('userid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.user')),
            ],
        ),
        migrations.AddField(
            model_name='hotel',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.locations'),
        ),
        migrations.AddField(
            model_name='hotel',
            name='login',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.login'),
        ),
        migrations.AddField(
            model_name='hotel',
            name='state',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.state'),
        ),
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('feedback_id', models.AutoField(primary_key=True, serialize=False)),
                ('feedback', models.CharField(max_length=500, verbose_name='feedback')),
                ('reply', models.CharField(max_length=500, verbose_name='reply')),
                ('userid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.user')),
            ],
        ),
        migrations.AddField(
            model_name='district',
            name='state',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.state'),
        ),
        migrations.CreateModel(
            name='complaint',
            fields=[
                ('complaint_id', models.AutoField(primary_key=True, serialize=False)),
                ('sub', models.CharField(max_length=200, verbose_name='sublect')),
                ('msg', models.CharField(max_length=500, verbose_name='message')),
                ('reply', models.CharField(max_length=500, verbose_name='reply')),
                ('staff', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.staff')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='hotel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.hotel'),
        ),
        migrations.AddField(
            model_name='cart',
            name='menu_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.menu'),
        ),
        migrations.AddField(
            model_name='cart',
            name='stock_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.menustock'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.user'),
        ),
        migrations.AddField(
            model_name='bill',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.user'),
        ),
    ]
