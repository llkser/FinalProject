package com.example.myapplication;

import android.Manifest;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.graphics.drawable.Drawable;
import android.net.Uri;
import android.os.Build;
import android.os.Bundle;
import android.provider.MediaStore;
import android.text.Html;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.CompoundButton;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.ActivityCompat;
import androidx.core.content.ContextCompat;
import androidx.core.content.FileProvider;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import com.facebook.binaryresource.FileBinaryResource;
import com.facebook.cache.common.SimpleCacheKey;
import com.facebook.drawee.backends.pipeline.Fresco;
import com.facebook.drawee.view.SimpleDraweeView;

import org.json.JSONException;
import org.json.JSONObject;

import okhttp3.Call;
import okhttp3.Callback;
import okhttp3.FormBody;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;

public class MainPageActivity extends AppCompatActivity implements View.OnClickListener {
    String[] permissions = new String[]{Manifest.permission.CAMERA, Manifest.permission.WRITE_EXTERNAL_STORAGE};
    List<String> mPermissionList = new ArrayList<>();
    private void checkPermission() {
        mPermissionList.clear();
        for (int i = 0; i < permissions.length; i++) {
            if (ContextCompat.checkSelfPermission(this, permissions[i]) != PackageManager.PERMISSION_GRANTED) {
                mPermissionList.add(permissions[i]);
            }
        }
        if (mPermissionList.isEmpty());
        else {
            String[] permissions = mPermissionList.toArray(new String[mPermissionList.size()]);
            ActivityCompat.requestPermissions(MainPageActivity.this, permissions, PERMISSION_REQUEST);
        }
    }

    @Override
    public void onRequestPermissionsResult(int requestCode, @NonNull String[] permissions, @NonNull int[] grantResults) {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults);
        switch (requestCode) {
            case PERMISSION_REQUEST:
                break;
            default:
                super.onRequestPermissionsResult(requestCode, permissions, grantResults);
                break;
        }
    }

    private static final int PERMISSION_REQUEST = 1;
    public static final int CHOOSE_PHOTO=2;
    public static final int TAKE_PHOTO = 3;
    public static final String Tag="Main_page_activity";

    private SimpleDraweeView preview;
    private Button album;
    private Button camera;
    private CheckBox metal_Co;
    private CheckBox metal_Hg;
    private CheckBox metal_Ni;
    private Button confirm;
    private Uri imageUri;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        checkPermission();
        super.onCreate(savedInstanceState);
        Fresco.initialize(this);
        setContentView(R.layout.main_page_layout);
        preview=findViewById(R.id.preview);
        album=findViewById(R.id.album);
        camera=findViewById(R.id.camera);
        confirm=findViewById(R.id.confirm);
        metal_Co=findViewById(R.id.Metal_Co);
        metal_Hg=findViewById(R.id.Metal_Hg);
        metal_Ni=findViewById(R.id.Metal_Ni);
        metal_Co.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener(){
            @Override
            public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {
                if(isChecked){
                    metal_Hg.setChecked(false);
                    metal_Ni.setChecked(false);
                }
            }
        });
        metal_Hg.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener(){
            @Override
            public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {
                if(isChecked){
                    metal_Co.setChecked(false);
                    metal_Ni.setChecked(false);
                }
            }
        });
        metal_Ni.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener(){
            @Override
            public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {
                if(isChecked){
                    metal_Hg.setChecked(false);
                    metal_Co.setChecked(false);
                }
            }
        });

        album.setOnClickListener(this);
        camera.setOnClickListener(this);
        confirm.setOnClickListener(this);
    }

    @Override
    public void onClick(View v) {
        switch (v.getId()) {
            case R.id.album:
                openAlbum();
                break;
            case R.id.camera:
                openCamera();
                break;
            case R.id.confirm:
                sendPhoto();
                break;
        }
    }

    private void openAlbum(){
        Intent intent=new Intent("android.intent.action.GET_CONTENT");
        intent.setType("image/*");
        startActivityForResult(intent,CHOOSE_PHOTO);
    }

    private void openCamera(){
        File outputImage = new File(getExternalCacheDir(), "output_image.jpg");
        try {
            if (outputImage.exists()) {
                outputImage.delete();
            }
            outputImage.createNewFile();
        } catch (IOException e) {
            e.printStackTrace();
        }
        if(Build.VERSION.SDK_INT>=24){
            imageUri= FileProvider.getUriForFile(MainPageActivity.this,
                    "com.example.cameraalbumtest.fileprovider",outputImage);
        }else{
            imageUri=Uri.fromFile(outputImage);
        }
        Intent intent=new Intent("android.media.action.IMAGE_CAPTURE");
        intent.putExtra(MediaStore.EXTRA_OUTPUT,imageUri);
        startActivityForResult(intent,TAKE_PHOTO);
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        switch (requestCode){
            case CHOOSE_PHOTO:
                if(data!=null)
                {
                    imageUri=data.getData();
                    preview.setImageURI(imageUri);
                }
                else{
                    imageUri=null;
                    showToast("Please choose a photo!");
                }
                break;
            case TAKE_PHOTO:
                if(resultCode==RESULT_OK){
                    preview.setImageURI(imageUri);
                }
                else{
                    imageUri=null;
                    showToast("Please take a photo!");
                }
                break;
            default:
                break;
        }
    }

    private void sendPhoto(){
        if(imageUri!=null)
        {
            if(!metal_Co.isChecked()&&!metal_Hg.isChecked()&&!metal_Ni.isChecked())
            {
                showToast("Please choose a metal!");
                return;
            }
            try {
                Bitmap bitmap = MediaStore.Images.Media.getBitmap(getContentResolver(), imageUri);
                String picture=new Base64Util().bitmapToBase64(bitmap);

                OkHttpClient client = new OkHttpClient();
                FormBody.Builder formBuilder = new FormBody.Builder();
                formBuilder.add("image", picture);
                if(metal_Co.isChecked())
                    formBuilder.add("metalCode", "1");
                else if(metal_Hg.isChecked())
                    formBuilder.add("metalCode", "2");
                else
                    formBuilder.add("metalCode", "3");
                Request request = new Request.Builder().url("http://llkserfinal.pythonanywhere.com/test").post(formBuilder.build()).build();
                final Call call = client.newCall(request);
                call.enqueue(new Callback()
                {
                    @Override
                    public void onFailure(Call call, final IOException e)
                    {
                        runOnUiThread(new Runnable()
                        {
                            @Override
                            public void run() {
                                showToast("Can not connect to networks！");
                            }
                        });
                    }
                    @Override
                    public void onResponse(Call call, final Response response) throws IOException
                    {
                        final String res = response.body().string();
                        runOnUiThread(new Runnable()
                        {
                            @Override
                            public void run()
                            {
                                try {
                                    JSONObject res_inform = new JSONObject(res);
                                    Log.d(Tag,res_inform.toString());
                                    Intent intent = new Intent(MainPageActivity.this,ResultPageActivity.class);
                                    intent.putExtra("result","1-10 PPM");
                                    startActivityForResult(intent,1);
                                } catch (JSONException e) {
                                    e.printStackTrace();
                                }
                            }
                        });
                    }
                });
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
        else
            showToast("Please choose a photo!");
    }

    private void showToast(String str) {
        Toast.makeText(MainPageActivity.this,str,Toast.LENGTH_SHORT).show();
    }
}

